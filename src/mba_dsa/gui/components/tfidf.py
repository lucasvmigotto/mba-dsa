from typing import Self

from pydantic import computed_field

from ...schemas.enums.emojis import EmojisType
from ...schemas.inputs import TFIDFInputs
from ..components._base import Accordion, Label, Number
from ._base import BasePage_


class BaseTFIDF_(BasePage_):
    _DEFAULTS = TFIDFInputs()

    title: Label = Label(
        emoji=EmojisType.TF_IDF,
        text="tf-idf",
    )

    label_features: Label = Label(
        emoji=EmojisType.FEATURES,
        text="Max features",
    )

    label_min_df: Label = Label(
        emoji=EmojisType.MIN,
        text="DF min",
    )
    label_max_df: Label = Label(
        emoji=EmojisType.MAX,
        text="DF max",
    )

    label_min_ngram: Label = Label(
        emoji=EmojisType.MIN,
        text="n-gram min",
    )
    label_max_ngram: Label = Label(
        emoji=EmojisType.MAX,
        text="n-gram max",
    )

    label_score_limit: Label = Label(
        emoji=EmojisType.LIMIT,
        text="score limit",
    )
    label_score_threshold: Label = Label(
        emoji=EmojisType.THRESHOLD,
        text="score threshold",
    )

    @computed_field
    @property
    def label_tf_idf(self: Self, /) -> Label:
        return Label(
            emoji="\U0001f9ee",  # 🧮
            text="TF-IDF",
            titlelize=False,
        )

    @computed_field
    @property
    def accordion_tf_idf(self: Self, /) -> Accordion:
        return Accordion(
            label=self.label_tf_idf,
        )

    @computed_field
    @property
    def number_features(self: Self, /) -> Number:
        return Number(
            label=self.label_features,
            value=self._DEFAULTS.max_features,
        )

    @computed_field
    @property
    def number_min_df(self: Self, /) -> Number:
        return Number(
            label=self.label_min_df,
            value=self._DEFAULTS.min_df,
        )

    @computed_field
    @property
    def number_max_df(self: Self, /) -> Number:
        return Number(
            label=self.label_max_df,
            value=self._DEFAULTS.max_df,
        )

    @computed_field
    @property
    def number_min_ngram(self: Self, /) -> Number:
        return Number(
            label=self.label_min_ngram,
            value=self._DEFAULTS.ngram_range_min,
        )

    @computed_field
    @property
    def number_max_ngram(self: Self, /) -> Number:
        return Number(
            label=self.label_max_ngram,
            value=self._DEFAULTS.ngram_range_max,
        )

    @computed_field
    @property
    def number_score_limit(self: Self, /) -> Number:
        return Number(
            label=self.label_score_limit,
            value=self._DEFAULTS.score_limit,
        )

    @computed_field
    @property
    def number_score_threshold(self: Self, /) -> Number:
        return Number(
            label=self.label_score_threshold,
            value=self._DEFAULTS.score_threshold,
        )
