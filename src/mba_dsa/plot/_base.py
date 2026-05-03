from abc import ABC
from io import BytesIO
from typing import Self, Sequence, Type

from matplotlib.colors import to_hex
from matplotlib.figure import Figure as MatplotFigure
from matplotlib.pyplot import get_cmap
from networkx import DiGraph, Graph
from PIL.Image import Image
from PIL.Image import open as pil_open
from PIL.ImageFile import ImageFile
from plotly.graph_objects import Figure
from polars import DataFrame

from ..schemas.enums.plot import ImageFormatType


class PlotterBase_(ABC):
    _palette: Sequence[str] = list(
        map(
            to_hex,
            get_cmap("tab20")(range(20)),
        )
    )

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

    @classmethod
    def graph(
        cls: Type[Self],
        graph: Graph | DiGraph,
        /,
        *args,
        **kwargs,
    ) -> str:
        raise NotImplementedError()

    @classmethod
    async def graph_async(
        cls: Type[Self],
        graph: Graph | DiGraph,
        /,
        *args,
        **kwargs,
    ) -> str:
        return cls.graph(graph)

    @classmethod
    def plot(cls: Type[Self], df: DataFrame, /, *axes: str) -> Figure:
        raise NotImplementedError()

    @classmethod
    def plot_async(cls: Type[Self], df: DataFrame, /, *axes: str) -> Figure:
        return cls.plot(df)

    @classmethod
    def image(
        cls: Type[Self],
        corpus: Sequence[str],
        /,
        *args,
        **kwargs,
    ) -> Image:
        raise NotImplementedError()

    @classmethod
    async def image_async(
        cls: Type[Self],
        corpus: Sequence[str],
        /,
        *args,
        **kwargs,
    ) -> Image:
        return cls.image(corpus)
