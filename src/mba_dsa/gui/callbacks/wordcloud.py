from typing import Self

from gradio import Image

from ...plot import WordCloudPlotter
from ...schemas.enums.inputs import BackgroundColorMode, ColorMap, ColorMode, SortOrder
from ...schemas.inputs import WordCloudInputs
from ...schemas.wordcloud import WordCloud
from ._base import OnCallbackBase


class WordCloudCallback(OnCallbackBase):
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
    ) -> Image:
        return Image(
            value=WordCloudPlotter.image(
                WordCloud.get_corpus(self._lf, dropdown_year),
                **WordCloudInputs(
                    max_features=tfidf_features,
                    score_limit=tfidf_score_limit,
                    score_threshold=tfidf_score_threshold,
                    score_filter=tfidf_score_sort,
                    min_df=tfidf_min_df,
                    max_df=tfidf_max_df,
                    ngram_range_min=tfidf_min_ngram,
                    ngram_range_max=tfidf_max_ngram,
                    ignore_words=ignore_words,
                    background_color_mode=background_color_mode,
                    colormap=colormap,
                    colormode=colormode,
                    max_words=max_words,
                    max_fontsize=max_fontsize,
                    plot_width=plot_width,
                    plot_height=plot_height,
                ).model_dump(),
            ),
        )
