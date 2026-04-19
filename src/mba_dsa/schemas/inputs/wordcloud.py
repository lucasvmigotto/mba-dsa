from ...settings.ui.wordcloud import (
    BackgroundColorChoiceSignType,
    ColorMapChoiceSignType,
    ColorModeChoiceSignType,
)
from .tfidf import TFIDFInputs


class WordCloudInputs(TFIDFInputs):
    ignore: str | None = ""
    background_color: BackgroundColorChoiceSignType = "white"
    colormap: ColorMapChoiceSignType = "tab20"
    colormode: ColorModeChoiceSignType = "RGB"
    max_words: int = 200
    max_fontsize: int = 100
    width: int = 800
    height: int = 800
