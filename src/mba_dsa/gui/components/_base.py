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

from ...schemas.enums import (
    DateTimeTypeOptions,
    ImageButtonsType,
    ImageFormatType,
    ImageModeType,
)


class BaseGUI_(BaseModel, ABC):
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        extra="ignore",
        use_enum_values=True,
    )


class BaseComponent_(BaseGUI_, ABC):
    def dump_(
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
    label: str
    titlelize: bool = True

    @computed_field
    @property
    def emoji_(self: Self, /) -> str:
        return f"{self.emoji} " if self.emoji else ""

    @computed_field
    @property
    def label_(self: Self, /) -> str:
        return self.label.title() if self.titlelize else self.label

    @computed_field
    @property
    def emoji_label(self: Self, /) -> str:
        return f"{self.emoji_}{self.label_}"

    def __str__(self: Self, /) -> str:
        return self.emoji_label

    @model_serializer(mode="plain")
    def ui_serializer(self: Self, /) -> str:
        return self.emoji_label


class Accordion(BaseComponent_):
    label: Label
    open: bool = False


class Dropdown(BaseComponent_):
    label: Label
    multiselect: bool = True
    filterable = True


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


class _BaseUIScreen(BaseGUI_, ABC):
    route: Optional[str] = None

    title: MarkdownHeader

    label_preferences: Label = Label(
        emoji="\U00002699",  # ⚙️
        label="configurações",
    )

    label_filters: Label = Label(
        emoji=label_preferences.emoji,
        label="filtros",
    )

    label_start: Label = Label(
        emoji="\U0001f4e2",  # 📢
        label="início",
    )

    label_end: Label = Label(
        emoji="\U0001f3c1",  # 🏁
        label="término",
    )

    label_add: Label = Label(
        emoji="\U00002795",  # ➕
        label="adicionar",
    )
    label_remove: Label = Label(
        emoji="\U00002796",  # ➖
        label="excluir",
    )

    label_create: Label = Label(
        emoji="\U0001fa84",  # 🪄
        label="criar",
    )

    label_search: Label = Label(
        emoji="\U0001f50e",  # 🔎
        label="buscar",
    )

    @computed_field
    @property
    def route_(self: Self, /) -> tuple[str, str]:
        return self.title.label.label_, self.route or self.title.label.label.lower()

    @computed_field
    @property
    def btn_create(self: Self, /) -> Button:
        return Button(label=self.label_create)
