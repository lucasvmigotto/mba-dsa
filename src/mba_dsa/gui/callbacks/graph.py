from typing import Self

from gradio import HTML

from ...plot import GraphPlotter
from ...schemas.enums.inputs import SizeUnit, SortOrder
from ...schemas.graph import Graph
from ...schemas.inputs import GraphInputs
from ._base import OnCallbackBase


class GraphCallback(OnCallbackBase):
    def on_btn_create_callback(
        self: Self,
        dropdown_year: int,
        tfidf_features: int,
        tfidf_score_limit: int,
        tfidf_score_threshold: int,
        tfidf_score_sort: SortOrder,
        tfidf_min_df: float | int,
        tfidf_max_df: float | int,
        tfidf_min_ngram: int,
        tfidf_max_ngram: int,
        directional: bool,
        nodes_distance: int,
        spring_length: int,
        width_value: int,
        width_unit: SizeUnit,
        height_value: int,
        height_unit: SizeUnit,
        /,
    ) -> HTML:

        return HTML(
            value=GraphPlotter.graph(
                Graph.build_graph(
                    self._lf,
                    dropdown_year,
                ),
                **GraphInputs(
                    max_features=tfidf_features,
                    score_limit=tfidf_score_limit,
                    score_threshold=tfidf_score_threshold,
                    score_filter=tfidf_score_sort,
                    min_df=tfidf_min_df,
                    max_df=tfidf_max_df,
                    ngram_range_min=tfidf_min_ngram,
                    ngram_range_max=tfidf_max_ngram,
                    directional=directional,
                    nodes_distance=nodes_distance,
                    spring_length=spring_length,
                    width_value=width_value,
                    width_unit=width_unit,
                    height_value=height_value,
                    height_unit=height_unit,
                ).model_dump(),
            )
        )
