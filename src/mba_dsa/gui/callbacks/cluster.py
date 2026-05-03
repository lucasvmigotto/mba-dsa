from typing import Self

from gradio import Plot

from ...plot import Scatter2dPlotter, Scatter3dPlotter
from ...schemas.cluster import Cluster
from ...schemas.enums.inputs import SortOrder
from ...schemas.inputs import ClusterInputs
from ._base import OnCallbackBase


class ClusterCallback(OnCallbackBase):
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
    ) -> tuple[Plot, Plot]:
        inputs = ClusterInputs(
            max_features=tfidf_features,
            score_limit=tfidf_score_limit,
            score_threshold=tfidf_score_threshold,
            score_filter=tfidf_score_sort,
            sublinear_tf=True,
            min_df=tfidf_min_df,
            max_df=tfidf_max_df,
            ngram_range_min=tfidf_min_ngram,
            ngram_range_max=tfidf_max_ngram,
            pca_components=pca_components,
            pca_seed=pca_seed,
            kmeans_n_clusters=kmeans_n_clusters,
            kmeans_seed=kmeans_seed,
        )
        df, *_ = Cluster.analysis(self._lf, dropdown_year)
        axes = [f"pca_{i}" for i in range(inputs.pca_components)]
        return (
            Plot(value=Scatter2dPlotter.plot(df, *axes, col_clusters="cluster")),
            Plot(value=Scatter3dPlotter.plot(df, *axes, col_clusters="cluster")),
        )
