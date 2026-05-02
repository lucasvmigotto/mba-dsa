from typing import Self

from ...schemas.enums.inputs import SizeUnit, SortOrder
from ._base import OnCallbackBase


class GraphCallback(OnCallbackBase):
    async def on_btn_create_callback_async(self: Self, /, *args, **kwargs):
        return self.on_btn_create_callback(*args, **kwargs)

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
    ):
        return None
