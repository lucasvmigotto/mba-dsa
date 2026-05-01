from typing import Self

from polars import LazyFrame

from ._base import OnCallbackBase


class GraphCallback(OnCallbackBase):
    async def on_btn_create_callback_async(self: Self, /):
        raise NotImplementedError()

    def on_btn_create_callback(self: Self, /):
        raise NotImplementedError()
