from typing import Self

from pydantic import computed_field

from ...schemas.enums.emojis import EmojisType
from ...schemas.inputs import ClusterInputs
from ..components._base import Label, Number, Tab
from .tfidf import BaseTFIDF_


class ClusterPage(BaseTFIDF_):
    _DEFAULTS = ClusterInputs()

    title: Label = Label(
        emoji=EmojisType.CLUSTER,
        text="cluster",
    )

    label_pca_components: Label = Label(
        emoji=EmojisType.COMPONENT,
        text="pca components",
    )

    label_pca_seed: Label = Label(
        emoji=EmojisType.SEED,
        text="pca seed",
    )

    label_kmeans_clusters: Label = Label(
        emoji=EmojisType.KMEANS_CLUSTER,
        text="kmeans clusters",
    )

    label_kmeans_seed: Label = Label(
        emoji=EmojisType.SEED,
        text="kmeans seed",
    )

    label_2d: Label = Label(
        emoji=EmojisType.TWO_D,
        text="2D",
        titlelize=False,
    )

    label_3d: Label = Label(
        emoji=EmojisType.THREE_D,
        text="3D",
        titlelize=False,
    )

    @computed_field
    @property
    def number_pca_components(self: Self, /) -> Number:
        return Number(
            label=self.label_pca_components,
            value=self._DEFAULTS.pca_components,
        )

    @computed_field
    @property
    def number_pca_seed(self: Self, /) -> Number:
        return Number(
            label=self.label_pca_seed,
            value=self._DEFAULTS.pca_seed,
        )

    @computed_field
    @property
    def number_kmeans_clusters(self: Self, /) -> Number:
        return Number(
            label=self.label_kmeans_clusters,
            value=self._DEFAULTS.kmeans_n_clusters,
        )

    @computed_field
    @property
    def number_kmeans_seed(self: Self, /) -> Number:
        return Number(
            label=self.label_kmeans_seed,
            value=self._DEFAULTS.kmeans_seed,
        )

    @computed_field
    @property
    def tab_2d(self: Self, /) -> Tab:
        return Tab(label=self.label_2d)

    @computed_field
    @property
    def tab_3d(self: Self, /) -> Tab:
        return Tab(label=self.label_3d)
