from typing import Optional, Self, Type

from polars import DataFrame, LazyFrame
from scipy.sparse import csr_matrix
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer

from ..utils import timeit
from ._base import BaseDataEntry_, FilterByYearType
from .inputs import ClusterInputs, TFIDFInputs


class Cluster(BaseDataEntry_):
    @timeit
    @classmethod
    def decomposition(
        cls: Type[Self],
        data: csr_matrix,
        /,
        components: int,
        seed: Optional[float | int] = None,
        col_name_prefix: str = "pca_",
    ) -> tuple[DataFrame, PCA]:
        return DataFrame(
            data=(
                model := PCA(
                    n_components=components,
                    random_state=seed,
                )
            ).fit_transform(data),
            schema=[f"{col_name_prefix}{i}" for i in range(components)],
        ), model

    @timeit
    @classmethod
    def clustering(
        cls: Type[Self],
        data: csr_matrix,
        /,
        clusters: int,
        seed: Optional[float | int] = None,
        col_name: str = "cluster",
    ) -> tuple[DataFrame, KMeans]:
        return DataFrame(
            data=(
                model := KMeans(
                    n_clusters=clusters,
                    random_state=seed,
                ).fit(data)
            ).labels_,
            schema=[col_name],
        ), model

    @timeit
    @classmethod
    def analysis(
        cls: Type[Self],
        lf: LazyFrame,
        year: FilterByYearType,
        /,
        options: Optional[ClusterInputs] = None,
    ) -> tuple[DataFrame, TfidfVectorizer, PCA, KMeans]:
        options_: ClusterInputs = options or ClusterInputs()
        data, vec = cls.vectorize(
            cls.polars_to_sequence(
                (df := cls.pipeline(lf, year)),
                col_name="lemmas",
            ),
            options=TFIDFInputs(**options_.model_dump()),
        )
        pca, pca_model = cls.decomposition(
            data,
            components=options_.pca_components,
            seed=options_.pca_seed_,
        )
        clusters, kmeans_model = cls.clustering(
            data,
            clusters=options_.kmeans_n_clusters,
            seed=options_.kmeans_seed_,
        )
        return (
            df.hstack(pca).hstack(clusters),
            vec,
            pca_model,
            kmeans_model,
        )
