from typing import Self

from PIL.Image import Image

from ..plot import generate_wordcloud
from ..schemas._types import (
    OnWordCloudCallback,
    OnWordCloudCallbackFn,
    PolarsData,
    PolarsDataFrames,
)
from ..schemas.inputs import WordCloudInputs
from ..utils import corpus_from_dataframe, shard_by_year
from ._base import _BaseCallbackService


class WordCloudCallback(_BaseCallbackService):
    def on_load(
        self: Self,
        data: PolarsDataFrames,
        /,
        **kwargs,
    ):
        raise NotImplementedError()

    def on_callback(
        self: Self,
        data: PolarsData,
        /,
    ) -> OnWordCloudCallback:
        def _caller(props: WordCloudInputs, /) -> OnWordCloudCallbackFn:
            def _fn(year: int, /) -> Image:
                return generate_wordcloud(
                    corpus_from_dataframe(
                        shard_by_year(data, year),
                        "lemmas",
                    ),
                    ignore=[word.strip() for word in props.ignore.split(",")]
                    if props.ignore
                    else None,
                    background_color=props.background_color,
                    colormap=props.colormap,
                    mode=props.colormode,
                    max_words=props.max_words,
                    max_font_size=props.max_fontsize,
                    width=props.width,
                    height=props.height,
                    seed=props.seed,
                )

            return _fn

        return _caller
