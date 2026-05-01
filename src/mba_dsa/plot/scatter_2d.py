from typing import Self, Type

from plotly.graph_objects import Figure
from polars import DataFrame

from ._base import PlotterBase_


class Scatter2dPlotter(PlotterBase_):
    @classmethod
    def plot(cls: Type[Self], df: DataFrame, /, *axes: str) -> Figure:
        raise NotImplementedError()

    @classmethod
    async def plot_async(cls: Type[Self], df: DataFrame, /, *axes: str) -> Figure:
        return cls.plot(df)
