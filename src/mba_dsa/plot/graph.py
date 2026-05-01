from typing import Self, Type

from polars import DataFrame

from ._base import PlotterBase_


class GraphPlotter(PlotterBase_):
    @classmethod
    def html(cls: Type[Self], df: DataFrame, /) -> str:
        raise NotImplementedError()

    @classmethod
    async def html_async(cls: Type[Self], df: DataFrame, /) -> str:
        return cls.html(df)
