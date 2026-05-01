from typing import Optional, Self, Sequence, Type

from networkx import DiGraph as DiGraphNx
from networkx import Graph as GraphNx
from polars import DataFrame, LazyFrame

from ..utils import timeit
from ._base import BaseDataEntry_, FilterByYearType
from .inputs import GraphInputs, TFIDFInputs


class Graph(BaseDataEntry_):
    @timeit
    @classmethod
    def nodes_from_ngrams(
        cls: Type[Self],
        ngrams: DataFrame,
        /,
        col_name: str,
    ) -> dict[str, set[str]]:
        nodes: dict[str, set[str]] = {}
        ngrams_: Sequence[str] = cls.polars_to_sequence(
            ngrams,
            col_name=col_name,
        )
        for parent in set([bigram.split(" ")[0] for bigram in ngrams_]):
            for child in [
                bigram.split(" ")[-1] for bigram in ngrams_ if bigram.startswith(parent)
            ]:
                if not nodes.get(child):
                    nodes[child] = set()
                nodes[child].add(parent)

        return nodes

    @timeit
    @classmethod
    def graph_from_nodes(
        cls: Type[Self],
        nodes: dict[str, set[str]],
        /,
        options: Optional[GraphInputs] = None,
    ) -> GraphNx | DiGraphNx:
        options_: GraphInputs = options or GraphInputs()
        graph = (DiGraphNx if options_.directional else GraphNx)()

        for node, edges in nodes.items():
            for edge in edges:
                graph.add_edge(edge, node)

        return graph

    @timeit
    @classmethod
    def build_graph(
        cls: Type[Self],
        lf: LazyFrame,
        year: FilterByYearType,
        /,
        options: Optional[GraphInputs] = None,
    ) -> GraphNx | DiGraphNx:
        options_: GraphInputs = options or GraphInputs()
        data, vec = cls.vectorize(
            cls.polars_to_sequence(
                cls.pipeline(lf, year),
                col_name="lemmas",
            ),
            options=(tfidf_options := TFIDFInputs(**options_.model_dump())),
        )
        return cls.graph_from_nodes(
            cls.nodes_from_ngrams(
                cls.features_from_vectors(
                    data,
                    vec,
                    options=tfidf_options,
                ),
                col_name="score",
            ),
            options=options_,
        )
