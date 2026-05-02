from abc import ABC
from typing import Annotated, Any, Literal, Optional, Self, Sequence

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PlainSerializer,
    PositiveInt,
    computed_field,
    model_serializer,
)

from ...schemas.enums.components import DateTimeTypeOptions, ImageButtonsType
from ...schemas.enums.emojis import EmojisType
from ...schemas.enums.inputs import (
    BackgroundColorMode,
    ColorMap,
    ColorMode,
    SizeUnit,
    SortOrder,
)
from ...schemas.enums.plot import ImageFormatType, ImageModeType


class BaseGUI_(BaseModel, ABC):
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        extra="ignore",
        use_enum_values=True,
    )


class BaseComponent_(BaseGUI_, ABC):
    def dump(
        self: Self,
        /,
        exclude: Optional[set[str]] = None,
    ) -> dict[str, Any]:
        return self.model_dump(
            exclude_computed_fields=True,
            exclude=exclude,
        )


class Label(BaseComponent_):
    emoji: Optional[str] = None
    text: str
    titlelize: bool = True

    @computed_field
    @property
    def emoji_(self: Self, /) -> str:
        return f"{self.emoji} " if self.emoji else ""

    @computed_field
    @property
    def text_(self: Self, /) -> str:
        return self.text.title() if self.titlelize else self.text

    @computed_field
    @property
    def text_clean(self: Self, /) -> str:
        return self.text.lower().replace(" ", "-").strip()

    @computed_field
    @property
    def emoji_text(self: Self, /) -> str:
        return f"{self.emoji_}{self.text_}"

    def __str__(self: Self, /) -> str:
        return self.emoji_text

    @model_serializer(mode="plain")
    def ui_serializer(self: Self, /) -> str:
        return self.emoji_text


class Accordion(BaseComponent_):
    label: Label
    open: bool = False


class Dropdown(BaseComponent_):
    value: Optional[str] = None
    label: Label
    multiselect: bool = False
    filterable: bool = True
    choices: Optional[Sequence[tuple[str, str]] | Sequence[str]] = None


class Image(BaseComponent_):
    label: Label
    buttons: Sequence[ImageButtonsType] = [
        ImageButtonsType.FULLSCREEN,
        ImageButtonsType.DOWNLOAD,
    ]
    format: ImageFormatType = ImageFormatType.PNG
    image_mode: ImageModeType = ImageModeType.MODE_RGB


class Button(BaseComponent_):
    label: Label

    @model_serializer(mode="plain")
    def ui_serializer(self: Self, /) -> dict[str, str]:
        return {
            "value": f"{self.label}",
        }


class MarkdownHeader(BaseComponent_):
    label: Label
    level: PositiveInt = Field(
        default=1,
        gt=0,
        lt=7,
    )

    @model_serializer(mode="plain")
    def ui_serializer(self: Self, /) -> dict[str, str]:
        return {
            "value": f"{'#' * self.level} {self.label}",
        }


class Tab(BaseComponent_):
    label: Label


class DateTime(BaseComponent_):
    label: Label
    include_time: bool = True
    type: DateTimeTypeOptions = DateTimeTypeOptions.DATETIME


class Number(BaseComponent_):
    label: Label
    value: Optional[float | int] = None
    minimum: Optional[float | int] = None
    maximum: Optional[float | int] = None


type SliderPrecisionType_ = Annotated[
    Optional[Literal["0"]],
    PlainSerializer(func=int),
]


class Slider(Number):
    precision: SliderPrecisionType_ = None
    step: Optional[float] = None


class Checkbox(BaseComponent_):
    label: Label


class Text(BaseComponent_):
    label: Label
    value: Optional[str] = None


class BasePage_(BaseGUI_, ABC):
    route: Optional[str] = None

    title: Label

    label_year_filer: Label = Label(
        emoji=EmojisType.YEAR_FILTER,
        text="year filter",
    )

    label_preferences: Label = Label(
        emoji=EmojisType.CONFIG,
        text="preferences",
    )

    label_filters: Label = Label(
        emoji=EmojisType.CONFIG,
        text="filters",
    )

    label_start: Label = Label(
        emoji=EmojisType.START,
        text="start",
    )

    label_end: Label = Label(
        emoji=EmojisType.END,
        text="end",
    )

    label_add: Label = Label(
        emoji=EmojisType.ADD,
        text="adicionar",
    )
    label_remove: Label = Label(
        emoji=EmojisType.END,
        text="remove",
    )

    label_create: Label = Label(
        emoji=EmojisType.CREATE,
        text="create",
    )

    label_search: Label = Label(
        emoji=EmojisType.SEARCH,
        text="search",
    )

    label_width: Label = Label(
        emoji=EmojisType.WIDTH,
        text="width",
    )

    label_height: Label = Label(
        emoji=EmojisType.HEIGHT,
        text="height",
    )

    label_unit: Label = Label(
        emoji=EmojisType.UNIT,
        text="unit",
    )

    label_sort: Label = Label(
        emoji=EmojisType.SORT,
        text="sort order",
    )

    label_colormap: Label = Label(
        emoji=EmojisType.COLOR_MAP,
        text="color map",
    )

    label_colormode: Label = Label(
        emoji=EmojisType.COLOR_MODE,
        text="color mode",
    )

    label_background_color_mode: Label = Label(
        emoji=EmojisType.BACKGROUND_COLOR_MODE,
        text="background color mode",
    )

    label_seed: Label = Label(
        emoji=EmojisType.SEED,
        text="seed",
    )

    @computed_field
    @property
    def route_(self: Self, /) -> tuple[str, str]:
        return (
            self.title.emoji_text if self.title else "main",
            self.route or self.title.text_clean if self.title else "",
        )

    @computed_field
    @property
    def md_title(self: Self, /) -> MarkdownHeader:
        return MarkdownHeader(label=self.title)

    @computed_field
    @property
    def dropdown_year_filter(self: Self, /) -> Dropdown:
        return Dropdown(label=self.label_year_filer)

    @computed_field
    @property
    def accordion_preferences(self: Self, /) -> Accordion:
        return Accordion(label=self.label_preferences)

    @computed_field
    @property
    def accordion_filters(self: Self, /) -> Accordion:
        return Accordion(label=self.label_filters)

    @computed_field
    @property
    def dropdown_unit(self: Self, /) -> Dropdown:
        return Dropdown(
            label=self.label_unit,
            choices=SizeUnit.as_choices(),
        )

    @computed_field
    @property
    def dropdown_sort(self: Self, /) -> Dropdown:
        return Dropdown(
            label=self.label_sort,
            choices=SortOrder.as_choices(),
            value=SortOrder.DESC,
        )

    @computed_field
    @property
    def dropdown_colormap(self: Self, /) -> Dropdown:
        return Dropdown(
            label=self.label_colormap,
            choices=ColorMap.as_choices(),
            value=ColorMap.TAB20,
        )

    @computed_field
    @property
    def dropdown_colormode(self: Self, /) -> Dropdown:
        return Dropdown(
            label=self.label_colormode,
            choices=ColorMode.as_choices(),
            value=ColorMode.RGB,
        )

    @computed_field
    @property
    def dropdown_background_color_mode(self: Self, /) -> Dropdown:
        return Dropdown(
            label=self.label_background_color_mode,
            choices=BackgroundColorMode.as_choices(),
            value=BackgroundColorMode.LIGHT,
        )

    @computed_field
    @property
    def btn_create(self: Self, /) -> Button:
        return Button(label=self.label_create)

    @computed_field
    @property
    def number_seed(self: Self, /) -> Number:
        return Number(label=self.label_seed)
