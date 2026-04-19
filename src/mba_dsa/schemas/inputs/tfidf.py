from ...settings.ui._commons import SortOrderChoiceSignType
from ._commons import InputsCommons


class TFIDFInputs(InputsCommons):
    vec_max_features: int = 10_000
    vec_score_threshold: int = 100
    vec_score_limit: int = 1000
    vec_score_sort: SortOrderChoiceSignType = "desc"
