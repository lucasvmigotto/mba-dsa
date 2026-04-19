from typing import Self

from polars import DataFrame
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from ..data import tf_idf
from ..plot import plot_scatter_2d, plot_scatter_3d
from ..schemas._types import (
    OnClusterCallback,
    OnClusterCallbackFn,
    OnClusterCallbackReturn,
    PolarsData,
    PolarsDataFrames,
)
from ..schemas.inputs import ClusterInputs
from ..utils import from_figure_to_image, shard_by_year
from ._base import _BaseCallbackService


class ClusterCallback(_BaseCallbackService):
    def on_load(
        self: Self,
        data: PolarsDataFrames,
        /,
        **kwargs,
    ):
        raise NotImplementedError()

    def on_callback(
        self: Self,
        data: PolarsData,
        /,
    ) -> OnClusterCallback:
        def _callback(props: ClusterInputs, /) -> OnClusterCallbackFn:
            def _fn(year: int, /) -> OnClusterCallbackReturn:
                _df: DataFrame = shard_by_year(data, year).collect()

                features, _ = tf_idf(
                    _df.get_column("lemmas"),
                    ngram_range=props.ngram_range_,
                    min_df=props.min_df,
                    max_df=props.max_df,
                    sublinear_tf=True,
                )

                pca_vecs = DataFrame(
                    data=(
                        _pca_model := PCA(
                            n_components=props.pca_n_components,
                            random_state=props.random_state_kmeans,
                        )
                    ).fit_transform(features),
                    schema=[f"pca_{i}" for i in range(props.pca_n_components)],
                )

                clusters = DataFrame(
                    data=(
                        _kmeans := KMeans(
                            n_clusters=props.kmeans_n_clusters,
                            random_state=props.random_state_kmeans,
                        ).fit(features)
                    ).labels_,
                    schema=["cluster"],
                )

                _df: DataFrame = _df.hstack(pca_vecs).hstack(clusters)

                fig_2d, ax = plot_scatter_2d(
                    _df,
                    "pca_0",
                    "pca_1",
                    "cluster",
                    xaxis_is_visible=False,
                    yaxis_is_visible=False,
                )

                return (
                    (
                        from_figure_to_image(fig_2d),
                        None,
                    )
                    if props.pca_n_components < 3
                    else (
                        from_figure_to_image(fig_2d),
                        plot_scatter_3d(
                            _df,
                            "pca_0",
                            "pca_1",
                            "pca_2",
                            "cluster",
                        ),
                    )
                )

            return _fn

        return _callback
