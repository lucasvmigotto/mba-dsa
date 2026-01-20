from typing import Sequence

from networkx import DiGraph, Graph
from polars import DataFrame, Series

from ..utils.data import polars_to_sequence
from ..utils.decorators import timeit


@timeit
def init_nodes(
    bigrams: DataFrame | Series | Sequence[str], /, column_name: str | None = None
) -> dict[str, set[str]]:
    _bigrams = (
        polars_to_sequence(bigrams, column_name)
        if isinstance(bigrams, (DataFrame, Series))
        else bigrams
    )

    nodes: dict[str, set[str]] = {}
    for parent in set([bigram.split(" ")[0] for bigram in _bigrams]):
        for child in [
            bigram.split(" ")[-1] for bigram in _bigrams if bigram.startswith(parent)
        ]:
            if not nodes.get(child):
                nodes[child] = set()
            nodes[child].add(parent)

    return nodes


@timeit
def build_graph(
    nodes: dict[str, set[str]], /, directional: bool = False
) -> Graph | DiGraph:
    graph = (DiGraph if directional else Graph)()
    for node, edges in nodes.items():
        for edge in edges:
            graph.add_edge(edge, node)

    return graph
