from typing import Optional, Self

from pydantic import PositiveFloat, PositiveInt, computed_field

from ..enums.inputs import SortOrder
from ._base import BaseInput_


class TFIDFInputs(BaseInput_):
    max_features: PositiveInt = 10_000

    ngram_range_min: PositiveInt = 2
    ngram_range_max: PositiveInt = 2

    min_df: PositiveFloat | PositiveInt = 5
    max_df: PositiveFloat | PositiveInt = 0.95

    sublinear_tf: bool = False

    score_limit: PositiveInt = 100
    score_threshold: Optional[PositiveInt] = 100
    score_filter: SortOrder = SortOrder.DESC

    @computed_field
    @property
    def ngram_range(self: Self, /) -> tuple[int, int]:
        return self.ngram_range_min, self.ngram_range_max
