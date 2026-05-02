from abc import ABC
from typing import Self, Sequence, Type

from gradio import Dropdown
from polars import LazyFrame


class OnCallbackBase(ABC):
    @classmethod
    def years_sequence(cls: Type[Self], lf: LazyFrame, /) -> Sequence[str]:
        return (
            lf.select("year")
            .unique()
            .sort(by="year", descending=True)
            .collect()
            .get_column("year")  # ty:ignore[unresolved-attribute]
            .to_list()
        )

    def __init__(self: Self, lf: LazyFrame, /):
        self._lf: LazyFrame = lf
        self._years = self.years_sequence(self._lf)

    async def on_load_async(self: Self, /) -> Dropdown:
        return self.on_load()

    def on_load(self: Self, /) -> Dropdown:
        return Dropdown(choices=self._years, value=self._years[0])

    async def on_btn_create_callback_async(self: Self, /, *args, **kwargs):
        return self.on_btn_create_callback(*args, **kwargs)

    def on_btn_create_callback(self: Self, /, *args, **kwargs):
        return None
