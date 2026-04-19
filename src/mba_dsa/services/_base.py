from abc import ABC, abstractmethod
from typing import Any, Self

from ..schemas._types import OnCallback, PolarsData, PolarsDataFrames
from ..settings import Settings


class _BaseCallbackService(ABC):
    def __init__(self: Self, settings: Settings, /):
        pass

    @abstractmethod
    def on_load(
        self: Self,
        data: PolarsDataFrames,
        /,
        **kwargs,
    ) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def on_callback(
        self: Self,
        data: PolarsData,
        /,
    ) -> OnCallback:
        raise NotImplementedError()
