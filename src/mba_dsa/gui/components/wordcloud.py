from typing import Self

from pydantic import computed_field

from ...schemas.enums.emojis import EmojisType
from ...schemas.inputs import WordCloudInputs
from ..components._base import Label, Number, Text
from .tfidf import BaseTFIDF_


class WordCloudPage(BaseTFIDF_):
    _DEFAULTS = WordCloudInputs()

    title: Label = Label(
        emoji=EmojisType.WORDCLOUD,
        text="wordcloud",
    )

    label_ignore_words: Label = Label(
        emoji=EmojisType.IGNORE,
        text="ignore words",
    )

    label_max_words: Label = Label(
        emoji=EmojisType.COUNT,
        text="max words",
    )

    label_max_fontsize: Label = Label(
        emoji=EmojisType.FONTSIZE,
        text="max fontsize",
    )

    @computed_field
    @property
    def text_ignore_words(self: Self, /) -> Text:
        return Text(
            label=self.label_ignore_words,
            value=self._DEFAULTS.ignore_words,
        )

    @computed_field
    @property
    def number_max_words(self: Self, /) -> Number:
        return Number(
            label=self.label_max_words,
            value=self._DEFAULTS.max_words,
        )

    @computed_field
    @property
    def number_max_fontsize(self: Self, /) -> Number:
        return Number(
            label=self.label_max_fontsize,
            value=self._DEFAULTS.max_fontsize,
        )

    @computed_field
    @property
    def number_width(self: Self, /) -> Number:
        return Number(
            label=self.label_width,
            value=self._DEFAULTS.plot_width,
        )

    @computed_field
    @property
    def number_height(self: Self, /) -> Number:
        return Number(
            label=self.label_height,
            value=self._DEFAULTS.plot_height,
        )
