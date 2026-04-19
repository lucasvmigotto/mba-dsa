from typing import Any, Literal, Self, Sequence

from pydantic import computed_field

from ._commons import UICommons

type UnitChoiceSignType = Literal["%", "px"]
type UnitChoiceNameType = Literal["Percentage", "Pixels"]
type UnitChoiceOptionType = tuple[UnitChoiceNameType, UnitChoiceSignType]
type UnitChoicesType = Sequence[UnitChoiceOptionType]

_UNIT_CHOICES_VALUES: UnitChoicesType = [("Percentage", "%"), ("Pixels", "px")]


class GraphUISettings(UICommons):
    TITLE_EMOJI: str = "\U0001f578"  # 🕸️
    TITLE_LABEL: str = "Graph"
    NAV_TITLE: str = "Graph"
    NAV_PATH: str = "graph"

    GRAPH_NODES_DISTANCE_LABEL: str = "Distance between nodes"
    GRAPH_NODES_DISTANCE_MINIMUM: int = 0
    GRAPH_NODES_DISTANCE_VALUE: int = 75
    GRAPH_NODES_DISTANCE_PRECISION: int = 1
    GRAPH_NODES_DISTANCE_STEP: int = 5
    GRAPH_NODES_DISTANCE_INTERACTIVE: bool = True

    GRAPH_SPRING_LENGTH_LABEL: str = "Spring length"
    GRAPH_SPRING_LENGTH_MINIMUM: int = 0
    GRAPH_SPRING_LENGTH_VALUE: int = 75
    GRAPH_SPRING_LENGTH_PRECISION: int = 1
    GRAPH_SPRING_LENGTH_STEP: int = 5
    GRAPH_SPRING_LENGTH_INTERACTIVE: bool = True

    GRAPH_WIDTH_VALUE_LABEL: str = "Width Value"
    GRAPH_WIDTH_VALUE_MINIMUM: int = 100
    GRAPH_WIDTH_VALUE_VALUE: int = 100
    GRAPH_WIDTH_VALUE_STEP: int = 10
    GRAPH_WIDTH_VALUE_INTERACTIVE: bool = True
    GRAPH_WIDTH_VALUE_SCALE: int | None = 5

    GRAPH_WIDTH_UNIT_CHOICES: UnitChoicesType = _UNIT_CHOICES_VALUES
    GRAPH_WIDTH_UNIT_LABEL: str = "Width unit"
    GRAPH_WIDTH_UNIT_VALUE: UnitChoiceSignType = "%"
    GRAPH_WIDTH_UNIT_INTERACTIVE: bool = True

    GRAPH_HEIGHT_VALUE_LABEL: str = "Height Value"
    GRAPH_HEIGHT_VALUE_MINIMUM: int = 100
    GRAPH_HEIGHT_VALUE_VALUE: int = 700
    GRAPH_HEIGHT_VALUE_STEP: int = 10
    GRAPH_HEIGHT_VALUE_INTERACTIVE: bool = True
    GRAPH_HEIGHT_VALUE_SCALE: int = 5

    GRAPH_HEIGHT_UNIT_CHOICES: UnitChoicesType = _UNIT_CHOICES_VALUES
    GRAPH_HEIGHT_UNIT_LABEL: str = "Height unit"
    GRAPH_HEIGHT_UNIT_VALUE: UnitChoiceSignType = "px"
    GRAPH_HEIGHT_UNIT_INTERACTIVE: bool = True

    @computed_field
    @property
    def graph_nodes_distance_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.GRAPH_NODES_DISTANCE_LABEL,
            "minimum": self.GRAPH_NODES_DISTANCE_MINIMUM,
            "value": self.GRAPH_NODES_DISTANCE_VALUE,
            "precision": self.GRAPH_NODES_DISTANCE_PRECISION,
            "step": self.GRAPH_NODES_DISTANCE_STEP,
            "interactive": self.GRAPH_NODES_DISTANCE_INTERACTIVE,
        }

    @computed_field
    @property
    def graph_spring_length_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.GRAPH_SPRING_LENGTH_LABEL,
            "minimum": self.GRAPH_SPRING_LENGTH_MINIMUM,
            "value": self.GRAPH_SPRING_LENGTH_VALUE,
            "precision": self.GRAPH_SPRING_LENGTH_PRECISION,
            "step": self.GRAPH_SPRING_LENGTH_STEP,
            "interactive": self.GRAPH_SPRING_LENGTH_INTERACTIVE,
        }

    @computed_field
    @property
    def graph_width_value_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.GRAPH_WIDTH_VALUE_LABEL,
            "minimum": self.GRAPH_WIDTH_VALUE_MINIMUM,
            "value": self.GRAPH_WIDTH_VALUE_VALUE,
            "step": self.GRAPH_WIDTH_VALUE_STEP,
            "interactive": self.GRAPH_WIDTH_VALUE_INTERACTIVE,
            "scale": self.GRAPH_WIDTH_VALUE_SCALE,
        }

    @computed_field
    @property
    def graph_width_unit_props(self: Self) -> dict[str, Any]:
        return {
            "choices": self.GRAPH_WIDTH_UNIT_CHOICES,
            "label": self.GRAPH_WIDTH_UNIT_LABEL,
            "value": self.GRAPH_WIDTH_UNIT_VALUE,
            "interactive": self.GRAPH_WIDTH_UNIT_INTERACTIVE,
        }

    @computed_field
    @property
    def graph_height_value_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.GRAPH_HEIGHT_VALUE_LABEL,
            "minimum": self.GRAPH_HEIGHT_VALUE_MINIMUM,
            "value": self.GRAPH_HEIGHT_VALUE_VALUE,
            "step": self.GRAPH_HEIGHT_VALUE_STEP,
            "interactive": self.GRAPH_HEIGHT_VALUE_INTERACTIVE,
            "scale": self.GRAPH_HEIGHT_VALUE_SCALE,
        }

    @computed_field
    @property
    def graph_height_unit_props(self: Self) -> dict[str, Any]:
        return {
            "choices": self.GRAPH_HEIGHT_UNIT_CHOICES,
            "label": self.GRAPH_HEIGHT_UNIT_LABEL,
            "value": self.GRAPH_HEIGHT_UNIT_VALUE,
            "interactive": self.GRAPH_HEIGHT_UNIT_INTERACTIVE,
        }
