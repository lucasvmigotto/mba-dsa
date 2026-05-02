from typing import Self

from ...schemas.enums.inputs import BackgroundColorMode, ColorMap, ColorMode, SortOrder
from ._base import OnCallbackBase


class WordCloudCallback(OnCallbackBase):
    async def on_btn_create_callback_async(self: Self, /, *args, **kwargs):
        return self.on_btn_create_callback(*args, **kwargs)

    def on_btn_create_callback(
        self: Self,
        dropdown_year: int,
        tfidf_features: int,
        tfidf_score_limit: int,
        tfidf_score_threshold: int,
        tfidf_score_sort: SortOrder,
        tfidf_min_df: float | int,
        tfidf_max_df: float | int,
        tfidf_min_ngram: int,
        tfidf_max_ngram: int,
        ignore_words: str,
        background_color_mode: BackgroundColorMode,
        colormap: ColorMap,
        colormode: ColorMode,
        max_words: int,
        max_fontsize: int,
        plot_width: int,
        plot_height: int,
        /,
    ):
        return None
