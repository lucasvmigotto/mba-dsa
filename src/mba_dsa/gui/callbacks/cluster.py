from typing import Self

from ...schemas.enums.inputs import SortOrder
from ._base import OnCallbackBase


class ClusterCallback(OnCallbackBase):
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
        pca_components: int,
        pca_seed: float | int,
        kmeans_n_clusters: int,
        kmeans_seed: float | int,
        /,
    ):
        return None
