from typing import Any, Literal, Self, Sequence

from pydantic import computed_field

from ._commons import UICommons

type BackgroundColorChoiceSignType = Literal["dark", "white"]
type BackgroundColorChoiceNameType = Literal["Dark", "White"]
type BackgroundColorChoiceOptionType = tuple[
    BackgroundColorChoiceNameType, BackgroundColorChoiceSignType
]
type BackgroundColorChoicesType = Sequence[BackgroundColorChoiceOptionType]

type ColorMapChoiceSignType = Literal["tab20", "viridis"]
type ColorMapChoiceNameType = Literal["Tab 20", "Viridis"]
type ColorMapChoiceOptionType = tuple[ColorMapChoiceNameType, ColorMapChoiceSignType]
type ColorMapChoicesType = Sequence[ColorMapChoiceOptionType]

type ColorModeChoiceSignType = Literal["RGB", "RGBA"]
type ColorModeChoiceNameType = Literal["RGB", "RGBA"]
type ColorModeChoiceOptionType = tuple[ColorModeChoiceNameType, ColorModeChoiceSignType]
type ColorModeChoicesType = Sequence[ColorModeChoiceOptionType]

_BACKGROUND_COLOR_CHOICES_VALUES: BackgroundColorChoicesType = [
    ("Dark", "dark"),
    ("White", "white"),
]
_COLORMAP_CHOICES_VALUES: ColorMapChoicesType = [
    ("Tab 20", "tab20"),
    ("Viridis", "viridis"),
]
_COLORMODE_CHOICES_VALUES: ColorModeChoicesType = [("RGB", "RGB"), ("RGBA", "RGBA")]


class WordCloudUISettings(UICommons):
    TITLE_EMOJI: str = "\U00002601"  # ☁️
    TITLE_LABEL: str = "WordCloud"
    NAV_TITLE: str = "WordCloud"
    NAV_PATH: str = "wordcloud"

    WORDCLOUD_IGNORE_LABEL: str = "Ignore words"
    WORDCLOUD_IGNORE_PLACEHOLDER: str = "foo, bar, baz, ..."
    WORDCLOUD_IGNORE_VALUE: int | None = None
    WORDCLOUD_IGNORE_INTERACTIVE: bool = True

    WORDCLOUD_BACKGROUND_COLOR_CHOICES: BackgroundColorChoicesType = (
        _BACKGROUND_COLOR_CHOICES_VALUES
    )
    WORDCLOUD_BACKGROUND_COLOR_LABEL: str = "Background color"
    WORDCLOUD_BACKGROUND_COLOR_VALUE: BackgroundColorChoiceSignType = "white"
    WORDCLOUD_BACKGROUND_COLOR_INTERACTIVE: bool = True

    WORDCLOUD_COLORMAP_CHOICES: ColorMapChoicesType = _COLORMAP_CHOICES_VALUES
    WORDCLOUD_COLORMAP_LABEL: str = "Font color map"
    WORDCLOUD_COLORMAP_VALUE: ColorMapChoiceSignType = "tab20"
    WORDCLOUD_COLORMAP_INTERACTIVE: bool = True

    WORDCLOUD_COLORMODE_CHOICES: ColorModeChoicesType = _COLORMODE_CHOICES_VALUES
    WORDCLOUD_COLORMODE_LABEL: str = "Color mode"
    WORDCLOUD_COLORMODE_VALUE: ColorModeChoiceSignType = "RGB"
    WORDCLOUD_COLORMODE_INTERACTIVE: bool = True

    WORDCLOUD_MAX_WORDS_LABEL: str = "Max words"
    WORDCLOUD_MAX_WORDS_MINIMUM: int = 100
    WORDCLOUD_MAX_WORDS_MAXIMUM: int = 1_000
    WORDCLOUD_MAX_WORDS_VALUE: int = 200
    WORDCLOUD_MAX_WORDS_STEP: int = 10
    WORDCLOUD_MAX_WORDS_INTERACTIVE: int = True

    WORDCLOUD_MAX_FONTSIZE_LABEL: str = "Max font size"
    WORDCLOUD_MAX_FONTSIZE_MINIMUM: int = 10
    WORDCLOUD_MAX_FONTSIZE_VALUE: int = 100
    WORDCLOUD_MAX_FONTSIZE_INTERACTIVE: int = True

    WORDCLOUD_WIDTH_LABEL: str = "Plot width"
    WORDCLOUD_WIDTH_MINIMUM: int = 100
    WORDCLOUD_WIDTH_VALUE: int = 800
    WORDCLOUD_WIDTH_INTERACTIVE: int = True

    WORDCLOUD_HEIGHT_LABEL: str = "Plot height"
    WORDCLOUD_HEIGHT_MINIMUM: int = 100
    WORDCLOUD_HEIGHT_VALUE: int = 800
    WORDCLOUD_HEIGHT_INTERACTIVE: int = True

    @computed_field
    @property
    def wordcloud_ignore_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.WORDCLOUD_IGNORE_LABEL,
            "placeholder": self.WORDCLOUD_IGNORE_PLACEHOLDER,
            "value": self.WORDCLOUD_IGNORE_VALUE,
            "interactive": self.WORDCLOUD_IGNORE_INTERACTIVE,
        }

    @computed_field
    @property
    def wordcloud_background_color_props(self: Self) -> dict[str, Any]:
        return {
            "choices": self.WORDCLOUD_BACKGROUND_COLOR_CHOICES,
            "label": self.WORDCLOUD_BACKGROUND_COLOR_LABEL,
            "value": self.WORDCLOUD_BACKGROUND_COLOR_VALUE,
            "interactive": self.WORDCLOUD_BACKGROUND_COLOR_INTERACTIVE,
        }

    @computed_field
    @property
    def wordcloud_colormap_props(self: Self) -> dict[str, Any]:
        return {
            "choices": self.WORDCLOUD_COLORMAP_CHOICES,
            "label": self.WORDCLOUD_COLORMAP_LABEL,
            "value": self.WORDCLOUD_COLORMAP_VALUE,
            "interactive": self.WORDCLOUD_COLORMAP_INTERACTIVE,
        }

    @computed_field
    @property
    def wordcloud_colormode_props(self: Self) -> dict[str, Any]:
        return {
            "choices": self.WORDCLOUD_COLORMODE_CHOICES,
            "label": self.WORDCLOUD_COLORMODE_LABEL,
            "value": self.WORDCLOUD_COLORMODE_VALUE,
            "interactive": self.WORDCLOUD_COLORMODE_INTERACTIVE,
        }

    @computed_field
    @property
    def wordcloud_max_words_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.WORDCLOUD_MAX_WORDS_LABEL,
            "minimum": self.WORDCLOUD_MAX_WORDS_MINIMUM,
            "maximum": self.WORDCLOUD_MAX_WORDS_MAXIMUM,
            "value": self.WORDCLOUD_MAX_WORDS_VALUE,
            "step": self.WORDCLOUD_MAX_WORDS_STEP,
            "interactive": self.WORDCLOUD_MAX_WORDS_INTERACTIVE,
        }

    @computed_field
    @property
    def wordcloud_max_fontsize_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.WORDCLOUD_MAX_FONTSIZE_LABEL,
            "minimum": self.WORDCLOUD_MAX_FONTSIZE_MINIMUM,
            "value": self.WORDCLOUD_MAX_FONTSIZE_VALUE,
            "interactive": self.WORDCLOUD_MAX_FONTSIZE_INTERACTIVE,
        }

    @computed_field
    @property
    def wordcloud_width_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.WORDCLOUD_WIDTH_LABEL,
            "minimum": self.WORDCLOUD_WIDTH_MINIMUM,
            "value": self.WORDCLOUD_WIDTH_VALUE,
            "interactive": self.WORDCLOUD_WIDTH_INTERACTIVE,
        }

    @computed_field
    @property
    def wordcloud_height_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.WORDCLOUD_HEIGHT_LABEL,
            "minimum": self.WORDCLOUD_HEIGHT_MINIMUM,
            "value": self.WORDCLOUD_HEIGHT_VALUE,
            "interactive": self.WORDCLOUD_HEIGHT_INTERACTIVE,
        }
