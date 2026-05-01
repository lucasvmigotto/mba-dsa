from enum import StrEnum
from typing import Self, Sequence, Type


class AsChoice_(StrEnum):
    @classmethod
    def as_choices(cls: Type[Self], /) -> Sequence[tuple[str, str]]:
        return [(e.name.title(), e.value) for e in cls]


class SortOrder(AsChoice_):
    DESC = "desc"
    ASCD = "ascd"

    @property
    def is_descending(self: Self, /) -> bool:
        return self.value == self.DESC


class SizeUnit(AsChoice_):
    PERCENTAGE = "%"
    PIXELS = "px"


class BackgroundColorMode(AsChoice_):
    LIGHT = "white"
    DARK = "dark"


class ColorMap(AsChoice_):
    TAB20 = "tab20"
    VIRIDIS = "viridis"


class ColorMode(AsChoice_):
    RGB = "RGB"
    RGBA = "RGBA"
