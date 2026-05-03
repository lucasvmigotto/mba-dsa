from typing import Self, Sequence, Type

from PIL.Image import Image
from wordcloud import WordCloud

from ..schemas.inputs import WordCloudInputs
from ._base import PlotterBase_


class WordCloudPlotter(PlotterBase_):
    @classmethod
    def image(
        cls: Type[Self],
        corpus: Sequence[str],
        /,
        *args,
        **kwargs,
    ) -> Image:
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
