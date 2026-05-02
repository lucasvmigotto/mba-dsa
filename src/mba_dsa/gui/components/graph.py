from typing import Self

from pydantic import computed_field

from ...schemas.enums.emojis import EmojisType
from ...schemas.enums.inputs import SizeUnit
from ...schemas.inputs import GraphInputs
from ..components._base import Checkbox, Dropdown, Label, Number
from .tfidf import BaseTFIDF_


class GraphPage(BaseTFIDF_):
    _DEFAULTS = GraphInputs()

    title: Label = Label(
        emoji=EmojisType.GRAPH,
        text="graph",
    )

    label_directional: Label = Label(
        emoji=EmojisType.DIRECTIONAL,
        text="directional",
    )

    label_nodes_distance: Label = Label(
        emoji=EmojisType.DISTANCE,
        text="nodes distance",
    )

    label_spring_layout: Label = Label(
        emoji=EmojisType.LAYOUT,
        text="spring layout",
    )

    @computed_field
    @property
    def checkbox_directional(self: Self, /) -> Checkbox:
        return Checkbox(
            label=self.label_directional,
        )

    @computed_field
    @property
    def number_nodes_distance(self: Self, /) -> Number:
        return Number(
            label=self.label_nodes_distance,
            value=self._DEFAULTS.nodes_distance,
        )

    @computed_field
    @property
    def number_spring_layout(self: Self, /) -> Number:
        return Number(
            label=self.label_spring_layout,
            value=self._DEFAULTS.spring_length,
        )

    @computed_field
    @property
    def number_width(self: Self, /) -> Number:
        return Number(
            label=self.label_width,
            value=self._DEFAULTS.width_value,
        )

    @computed_field
    @property
    def dropdown_width(self: Self, /) -> Dropdown:
        return Dropdown(
            label=self.label_width,
            value=self._DEFAULTS.width_unit,
            choices=SizeUnit.as_choices(),
        )

    @computed_field
    @property
    def number_height(self: Self, /) -> Number:
        return Number(
            label=self.label_height,
            value=self._DEFAULTS.width_value,
        )

    @computed_field
    @property
    def dropdown_height(self: Self, /) -> Dropdown:
        return Dropdown(
            label=self.label_height,
            value=self._DEFAULTS.height_unit,
            choices=SizeUnit.as_choices(),
        )
