from abc import ABC
from io import BytesIO
from typing import Self, Sequence, Type

from matplotlib.colors import to_hex
from matplotlib.figure import Figure as MatplotFigure
from matplotlib.pyplot import get_cmap
from PIL.Image import open as pil_open
from PIL.ImageFile import ImageFile
from plotly.graph_objects import Figure
from polars import DataFrame

from ..schemas.enums import ImageFormatType

PALETTE_: Sequence[str] = list(
    map(
        to_hex,
        get_cmap("tab20")(range(20)),
    )
)


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

    @classmethod
    def html(cls: Type[Self], df: DataFrame, /) -> str:
        raise NotImplementedError()

    @classmethod
    async def html_async(cls: Type[Self], df: DataFrame, /) -> str:
        return cls.html(df)

    @classmethod
    def plot(cls: Type[Self], df: DataFrame, /, *axes: str) -> Figure:
        raise NotImplementedError()

    @classmethod
    async def plot_async(cls: Type[Self], df: DataFrame, /, *axes: str) -> Figure:
        return cls.plot(df)

    @classmethod
    def image(cls: Type[Self], df: DataFrame, /) -> ImageFile:
        raise NotImplementedError()

    @classmethod
    async def image_async(cls: Type[Self], df: DataFrame, /) -> ImageFile:
        return cls.image(df)
