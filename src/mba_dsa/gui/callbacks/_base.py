from abc import ABC
from typing import Self

from gradio import Dropdown
from polars import LazyFrame


class OnCallbackBase(ABC):
    def __init__(self: Self, lf: LazyFrame, /):
        self._lf: LazyFrame = lf

    async def on_load_async(self: Self, /):
        raise NotImplementedError()

    def on_load(self: Self, lf: LazyFrame, /):
        return Dropdown(
            choices=self._lf.select("year")
            .sort(by="year", descending=True)
            .collect()
            .get_column("year")  # ty:ignore[unresolved-attribute]
            .to_list()
        )

    async def on_btn_create_callback_async(self: Self, /):
        raise NotImplementedError()

    def on_btn_create_callback(self: Self, /):
        raise NotImplementedError()
