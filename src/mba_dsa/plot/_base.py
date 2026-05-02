from abc import ABC
from io import BytesIO
from typing import Self, Sequence, Type

from matplotlib.colors import to_hex
from matplotlib.figure import Figure as MatplotFigure
from matplotlib.pyplot import get_cmap
from networkx import DiGraph, Graph
from PIL.Image import open as pil_open
from PIL.ImageFile import ImageFile
from plotly.graph_objects import Figure
from polars import DataFrame

from ..schemas.enums.plot import ImageFormatType


class PlotterBase_(ABC):
    @classmethod
    def from_figure_to_image(
        cls: Type[Self],
        fig: MatplotFigure,
        /,
        image_format: ImageFormatType = ImageFormatType.PNG,
    ) -> ImageFile:
        def _fn():
            fig.savefig((buffer := BytesIO()), format=image_format)
            buffer.seek(0)
            yield pil_open(buffer)
            buffer.close()

        return next(_fn())

    def __init__(self: Self, /):
        self._palette: Sequence[str] = list(
            map(
                to_hex,
                get_cmap("tab20")(range(20)),
            )
        )

    def graph(
        self: Self,
        graph: Graph | DiGraph,
        /,
        *args,
        **kwargs,
    ) -> str:
        raise NotImplementedError()

    async def graph_async(
        self: Self,
        graph: Graph | DiGraph,
        /,
        *args,
        **kwargs,
    ) -> str:
        return self.graph(graph)

    def plot(self: Self, df: DataFrame, /, *axes: str) -> Figure:
        raise NotImplementedError()

    async def plot_async(self: Self, df: DataFrame, /, *axes: str) -> Figure:
        return self.plot(df)

    def image(
        self: Self,
        corpus: Sequence[str],
        /,
        *args,
        **kwargs,
    ) -> ImageFile:
        raise NotImplementedError()

    async def image_async(
        self: Self,
        corpus: Sequence[str],
        /,
        *args,
        **kwargs,
    ) -> ImageFile:
        return self.image(corpus)
