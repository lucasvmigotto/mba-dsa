from pydantic import PositiveInt

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
