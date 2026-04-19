from ...settings.ui.graph import UnitChoiceSignType
from .tfidf import TFIDFInputs


class GraphInputs(TFIDFInputs):
    nodes_distance: int = 75
    spring_length: int = 75
    width_value: int = 100
    width_unit: UnitChoiceSignType = "%"
    height_value: int = 700
    height_unit: UnitChoiceSignType = "px"
