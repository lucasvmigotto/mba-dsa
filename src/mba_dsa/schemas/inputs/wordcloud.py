from typing import Collection, Optional, Self

from pydantic import PositiveInt, computed_field

from ..enums.inputs import BackgroundColorMode, ColorMap, ColorMode
from .tfidf import TFIDFInputs


class WordCloudInputs(TFIDFInputs):
    ignore_words: Optional[str] = None

    background_color_mode: BackgroundColorMode = BackgroundColorMode.LIGHT
    colormap: ColorMap = ColorMap.TAB20
    colormode: ColorMode = ColorMode.RGB

    max_words: PositiveInt = 200
    max_fontsize: PositiveInt = 100

    plot_width: int = 800
    plot_height: int = 800

    @computed_field
    @property
    def ignore_words_(self: Self, /) -> Collection[str]:
        return (
            {w.lower() for w in self.ignore_words.split(";")}
            if self.ignore_words
            else {}
        )

    @computed_field
    @property
    def plot_size(self: Self, /) -> tuple[int, int]:
        return self.plot_width, self.plot_height
