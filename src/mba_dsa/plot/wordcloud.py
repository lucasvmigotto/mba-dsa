from typing import Self, Type

from PIL.ImageFile import ImageFile
from polars import DataFrame

from ._base import PlotterBase_


class WordCloudPlotter(PlotterBase_):
    @classmethod
    def image(cls: Type[Self], df: DataFrame, /) -> ImageFile:
        raise NotImplementedError()

    @classmethod
    async def image_async(cls: Type[Self], df: DataFrame, /) -> ImageFile:
        return cls.image(df)
