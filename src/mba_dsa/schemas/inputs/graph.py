from typing import Self

from pydantic import PositiveInt, computed_field

from ..enums.inputs import SizeUnit
from .tfidf import TFIDFInputs


class GraphInputs(TFIDFInputs):
    directional: bool = False

    nodes_distance: PositiveInt = 75
    spring_length: PositiveInt = 75

    width_value: PositiveInt = 100
    width_unit: SizeUnit = SizeUnit.PERCENTAGE

    height_value: PositiveInt = 700
    height_unit: SizeUnit = SizeUnit.PIXELS

    @computed_field
    @property
    def width_display(self: Self, /) -> str:
        return f"{self.width_value} {self.width_unit}"

    @computed_field
    @property
    def height_display(self: Self, /) -> str:
        return f"{self.height_value} {self.height_unit}"
