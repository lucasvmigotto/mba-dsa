from typing import Optional, Self

from pydantic import Field, PositiveInt, computed_field

from .tfidf import TFIDFInputs


class ClusterInputs(TFIDFInputs):
    pca_components: PositiveInt = Field(
        default=3,
        gt=1,
    )
    pca_seed: Optional[float | int] = None

    kmeans_n_clusters: PositiveInt = 3
    kmeans_seed: Optional[float | int] = None

    @computed_field
    @property
    def pca_seed_(self: Self, /) -> float | int:
        return self.pca_seed or self.seed

    @computed_field
    @property
    def kmeans_seed_(self: Self, /) -> float | int:
        return self.kmeans_seed or self.seed

    @computed_field
    @property
    def is_3d(self: Self, /) -> bool:
        return self.pca_components > 2
