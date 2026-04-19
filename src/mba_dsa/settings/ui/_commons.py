from typing import Any, Literal, Self, Sequence

from pydantic import computed_field

from .._base import _BaseSettings

type SortOrderChoiceSignType = Literal["desc", "ascd"]
type SorOrderChoiceNameType = Literal["Descending", "Ascending"]
type SorOrderChoiceOptionType = tuple[SorOrderChoiceNameType, SortOrderChoiceSignType]
type SorOrderChoicesType = Sequence[SorOrderChoiceOptionType]

_SORT_ORDER_CHOICES_VALUES: SorOrderChoicesType = [
    ("Ascending", "ascd"),
    ("Descending", "desc"),
]


class UICommons(_BaseSettings):
    TITLE_EMOJI: str = "\U00002753"  # ❓
    TITLE_LABEL: str = "Title goes here"
    NAV_TITLE: str = "Title goes here"
    NAV_PATH: str = "link-goes-here"

    PREFERENCES_ACCORDION_LABEL: str = "Preferences"
    PREFERENCES_ACCORDION_OPEN: bool = False

    PROCESS_DATA_BTN_LABEL: str = "Generate"
    PROCESS_DATA_BTN_scale: int | None = None

    DATA_DPD_LABEL: str = "Select a year to filter the results"
    DATA_DPD_INTERACTIVE: bool = True
    DATA_DPD_SCALE: int | None = None

    TF_IDF_MAX_FEATURES_LABEL: str = "TF-IDF Vectorizer features"
    TF_IDF_MAX_FEATURES_MINIMUM: int = 1_000
    TF_IDF_MAX_FEATURES_MAXIMUM: int = 20_000
    TF_IDF_MAX_FEATURES_VALUE: int = 10_000
    TF_IDF_MAX_FEATURES_STEP: int = 1_000
    TF_IDF_MAX_FEATURES_INTERACTIVE: bool = True

    TF_IDF_SCORE_THRESHOLD_LABEL: str = "Threshold value for TF-IDF score"
    TF_IDF_SCORE_THRESHOLD_MINIMUM: int = 0
    TF_IDF_SCORE_THRESHOLD_MAXIMUM: int = 1_000
    TF_IDF_SCORE_THRESHOLD_VALUE: int = 100
    TF_IDF_SCORE_THRESHOLD_PRECISION: int = 1
    TF_IDF_SCORE_THRESHOLD_STEP: int = 10
    TF_IDF_SCORE_THRESHOLD_INTERACTIVE: bool = True

    TF_IDF_SCORE_LIMIT_LABEL: str = "Limit up to N results from TF-IDF score"
    TF_IDF_SCORE_LIMIT_MINIMUM: int = 0
    TF_IDF_SCORE_LIMIT_VALUE: int = 1000
    TF_IDF_SCORE_LIMIT_PRECISION: int = 1
    TF_IDF_SCORE_LIMIT_STEP: int = 10
    TF_IDF_SCORE_LIMIT_INTERACTIVE: bool = True

    TF_IDF_SCORE_SORT_CHOICES: SorOrderChoicesType = _SORT_ORDER_CHOICES_VALUES
    TF_IDF_SCORE_SORT_LABEL: str = "Sort order for TF-IDF scores"
    TF_IDF_SCORE_SORT_VALUE: SortOrderChoiceSignType = "desc"
    TF_IDF_SCORE_SORT_INTERACTIVE: bool = True

    SEED_LABEL: str = "Seed"
    SEED_MINIMUM: int = 0
    SEED_VALUE: int = 42
    SEED_INTERACTIVE: int = True

    @computed_field
    @property
    def tf_idf_max_features_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.TF_IDF_MAX_FEATURES_LABEL,
            "minimum": self.TF_IDF_MAX_FEATURES_MINIMUM,
            "maximum": self.TF_IDF_MAX_FEATURES_MAXIMUM,
            "value": self.TF_IDF_MAX_FEATURES_VALUE,
            "step": self.TF_IDF_MAX_FEATURES_STEP,
            "interactive": self.TF_IDF_MAX_FEATURES_INTERACTIVE,
        }

    @computed_field
    @property
    def tf_idf_score_threshold_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.TF_IDF_SCORE_THRESHOLD_LABEL,
            "minimum": self.TF_IDF_SCORE_THRESHOLD_MINIMUM,
            "maximum": self.TF_IDF_SCORE_THRESHOLD_MAXIMUM,
            "value": self.TF_IDF_SCORE_THRESHOLD_VALUE,
            "precision": self.TF_IDF_SCORE_THRESHOLD_PRECISION,
            "step": self.TF_IDF_SCORE_THRESHOLD_STEP,
            "interactive": self.TF_IDF_SCORE_THRESHOLD_INTERACTIVE,
        }

    @computed_field
    @property
    def tf_idf_score_limit_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.TF_IDF_SCORE_LIMIT_LABEL,
            "minimum": self.TF_IDF_SCORE_LIMIT_MINIMUM,
            "value": self.TF_IDF_SCORE_LIMIT_VALUE,
            "precision": self.TF_IDF_SCORE_LIMIT_PRECISION,
            "step": self.TF_IDF_SCORE_LIMIT_STEP,
            "interactive": self.TF_IDF_SCORE_LIMIT_INTERACTIVE,
        }

    @computed_field
    @property
    def tf_idf_score_sort_props(self: Self) -> dict[str, Any]:
        return {
            "choices": self.TF_IDF_SCORE_SORT_CHOICES,
            "label": self.TF_IDF_SCORE_SORT_LABEL,
            "value": self.TF_IDF_SCORE_SORT_VALUE,
            "interactive": self.TF_IDF_SCORE_SORT_INTERACTIVE,
        }

    @computed_field
    @property
    def title_emoji(self: Self) -> str:
        return f"{self.TITLE_EMOJI} " if len(self.TITLE_EMOJI) else ""

    @computed_field
    @property
    def title_label(self: Self) -> str:
        return self.TITLE_LABEL

    @computed_field
    @property
    def title(self: Self) -> str:
        return f"{self.title_emoji} {self.title_label}"

    def title_md(self: Self, level: int = 1, /) -> str:
        return f"{'#' * level} {self.title}"

    @computed_field
    @property
    def navbar_props(self: Self) -> tuple[str, str]:
        return self.NAV_TITLE, self.NAV_PATH

    @computed_field
    @property
    def preferences_accordion_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.PREFERENCES_ACCORDION_LABEL,
            "open": self.PREFERENCES_ACCORDION_OPEN,
        }

    @computed_field
    @property
    def process_data_btn_props(self: Self) -> dict[str, Any]:
        return {
            "value": self.PROCESS_DATA_BTN_LABEL,
            "scale": self.PROCESS_DATA_BTN_scale,
        }

    @computed_field
    @property
    def data_dpd_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.DATA_DPD_LABEL,
            "interactive": self.DATA_DPD_INTERACTIVE,
            "scale": self.DATA_DPD_SCALE,
        }

    @computed_field
    @property
    def seed_props(self: Self) -> dict[str, Any]:
        return {
            "label": self.SEED_LABEL,
            "minimum": self.SEED_MINIMUM,
            "value": self.SEED_VALUE,
            "interactive": self.SEED_INTERACTIVE,
        }
