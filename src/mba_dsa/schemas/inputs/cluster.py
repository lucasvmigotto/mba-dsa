from typing import Self

from pydantic import computed_field

from ._commons import InputsCommons


class ClusterInputs(InputsCommons):
    ngram_range: int = 2
    min_df: float | int = 5
    max_df: float | int = 0.95
    sublinear_tf: bool = True
    pca_n_components: int = 2
    kmeans_n_clusters: int = 3
    random_state: int = 42
    random_state_pca: int | None = None
    random_state_kmeans: int | None = None

    @computed_field
    @property
    def ngram_range_(self: Self, /) -> tuple[int, int]:
        return (self.ngram_range, self.ngram_range)

    @computed_field
    @property
    def random_state_kmeans_(self: Self, /) -> int:
        return self.random_state_kmeans or self.random_state

    @computed_field
    @property
    def random_state_pca_(self: Self, /) -> int:
        return self.random_state_pca or self.random_state
