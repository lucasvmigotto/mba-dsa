from typing import Self, Type

from polars import LazyFrame

from ..utils import timeit
from ._base import BaseDataEntry_, FilterByYearType


class WordCloud(BaseDataEntry_):
    @timeit
    @classmethod
    def get_corpus(
        cls: Type[Self],
        lf: LazyFrame,
        year: FilterByYearType,
        /,
        **kwargs,
    ) -> str:
        return " ".join(
            cls.polars_to_sequence(
                cls.pipeline(lf, year, **kwargs),
                col_name="lemmas",
            )
        )
