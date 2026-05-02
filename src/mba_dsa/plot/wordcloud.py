from typing import Self, Sequence

from PIL.ImageFile import ImageFile
from wordcloud import WordCloud

from ..schemas.inputs import WordCloudInputs
from ._base import PlotterBase_


class WordCloudPlotter(PlotterBase_):
    def image(
        self: Self,
        corpus: Sequence[str],
        /,
        *args,
        **kwargs,
    ) -> ImageFile:
        inputs: WordCloudInputs = WordCloudInputs(**kwargs)
        return (
            WordCloud(
                stopwords=inputs.ignore_words_,
                background_color=inputs.background_color_mode,
                max_words=inputs.max_words,
                max_font_size=inputs.max_fontsize,
                width=inputs.plot_width,
                height=inputs.plot_height,
                colormap=inputs.colormap,
                random_state=inputs.seed,
                mode=inputs.colormode,
            )
            .generate(corpus)
            .to_image()
        )
