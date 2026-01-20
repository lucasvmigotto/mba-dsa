from typing import Literal, Sequence

from PIL.Image import Image
from wordcloud import WordCloud

from ..utils.decorators import timeit


@timeit
def generate_wordcloud(
    corpus: str,
    /,
    ignore: Sequence[str] | None | None = None,
    background_color: str | None = "white",
    max_words: int | None | None = None,
    max_font_size: int | None = 30,
    width: int | None = 800,
    height: int | None = 800,
    colormap: str | None = "tab10",
    mode: Literal["RGBA", "RGB"] | None = "RGB",
    seed: int | None = 42,
) -> Image:
    return (
        WordCloud(
            stopwords=ignore,
            background_color=background_color,
            max_words=max_words,
            max_font_size=max_font_size,
            width=width,
            height=height,
            colormap=colormap,
            random_state=seed,
            mode=mode,
        )
        .generate(corpus)
        .to_image()
    )
