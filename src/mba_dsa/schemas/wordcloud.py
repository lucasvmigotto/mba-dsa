from typing import Self, Type

from polars import LazyFrame

from ._base import BaseDataEntry_, FilterByYearType


class WordCloud(BaseDataEntry_):
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
