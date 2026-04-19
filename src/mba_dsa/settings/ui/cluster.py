from typing import Any, Self

from pydantic import computed_field

from ._commons import UICommons


class ClusterUISettings(UICommons):
    TITLE_EMOJI: str = "\U0001f4ca"  # 📊
    TITLE_LABEL: str = "Cluster"
    NAV_TITLE: str = "Cluster"
    NAV_PATH: str = "cluster"

    NGRAM_RANGE_LABEL: str = "N-Gram Range"
    NGRAM_RANGE_VALUE: int = 2
    NGRAM_RANGE_MINIMUM: int = 1
    NGRAM_RANGE_INTERACTIVE: bool = True

    MIN_DF_LABEL: str = "Minimum value for DF"
    MIN_DF_VALUE: float | int = 5
    MIN_DF_MINIMUM: float | int = 0.1
    MIN_DF_INTERACTIVE: bool = True

    MAX_DF_LABEL: str = "Maximum value for DF"
    MAX_DF_VALUE: float | int = 0.95
    MAX_DF_MAXIMUM: float | int = 1.0
    MAX_DF_INTERACTIVE: bool = True

    PCA_N_COMPONENTS_LABEL: str = "Number of PCA components"
    PCA_N_COMPONENTS_VALUE: int = 3
    PCA_N_COMPONENTS_MINIMUM: int = 2
    PCA_N_COMPONENTS_INTERACTIVE: bool = True

    KMEANS_N_CLUSTERS_LABEL: str = "Number of KMeans clusters"
    KMEANS_N_CLUSTERS_VALUE: int = 4
    KMEANS_N_CLUSTERS_MINIMUM: int = 2
    KMEANS_N_CLUSTERS_INTERACTIVE: bool = True

    RANDOM_STATE_LABEL: str = "Default seed"
    RANDOM_STATE_VALUE: int = 42
    RANDOM_STATE_INTERACTIVE: bool = True

    RANDOM_STATE_PCA_LABEL: str = "PCA seed"
    RANDOM_STATE_PCA_VALUE: int | None = None
    RANDOM_STATE_PCA_INTERACTIVE: bool = True

    RANDOM_STATE_KMEANS_LABEL: str = "KMeans seed"
    RANDOM_STATE_KMEANS_VALUE: int | None = None
    RANDOM_STATE_KMEANS_INTERACTIVE: bool = True

    TAB_2D_LABEL: str = "2D Cluster"
    TAB_3D_LABEL: str = "3D Cluster"

    @computed_field
    @property
    def tab_2d_label(self: Self) -> str:
        return self.TAB_2D_LABEL

    @computed_field
    @property
    def tab_3d_label(self: Self) -> str:
        return self.TAB_3D_LABEL

    @computed_field
    @property
    def ngram_range_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.NGRAM_RANGE_LABEL,
            "value": self.NGRAM_RANGE_VALUE,
            "interactive": self.NGRAM_RANGE_INTERACTIVE,
            "minimum": self.NGRAM_RANGE_MINIMUM,
        }

    @computed_field
    @property
    def min_df_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.MIN_DF_LABEL,
            "value": self.MIN_DF_VALUE,
            "interactive": self.MIN_DF_INTERACTIVE,
            "minimum": self.MIN_DF_MINIMUM,
        }

    @computed_field
    @property
    def max_df_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.MAX_DF_LABEL,
            "value": self.MAX_DF_VALUE,
            "interactive": self.MAX_DF_INTERACTIVE,
            "maximum": self.MAX_DF_MAXIMUM,
        }

    @computed_field
    @property
    def pca_n_components_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.PCA_N_COMPONENTS_LABEL,
            "value": self.PCA_N_COMPONENTS_VALUE,
            "interactive": self.PCA_N_COMPONENTS_INTERACTIVE,
            "minimum": self.PCA_N_COMPONENTS_MINIMUM,
        }

    @computed_field
    @property
    def kmeans_n_clusters_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.KMEANS_N_CLUSTERS_LABEL,
            "value": self.KMEANS_N_CLUSTERS_VALUE,
            "interactive": self.KMEANS_N_CLUSTERS_INTERACTIVE,
            "minimum": self.KMEANS_N_CLUSTERS_MINIMUM,
        }

    @computed_field
    @property
    def random_state_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.RANDOM_STATE_LABEL,
            "value": self.RANDOM_STATE_VALUE,
            "interactive": self.RANDOM_STATE_INTERACTIVE,
        }

    @computed_field
    @property
    def random_state_pca_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.RANDOM_STATE_PCA_LABEL,
            "value": self.RANDOM_STATE_PCA_VALUE,
            "interactive": self.RANDOM_STATE_PCA_INTERACTIVE,
        }

    @computed_field
    @property
    def random_state_kmeans_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.RANDOM_STATE_KMEANS_LABEL,
            "value": self.RANDOM_STATE_KMEANS_VALUE,
            "interactive": self.RANDOM_STATE_KMEANS_INTERACTIVE,
        }
