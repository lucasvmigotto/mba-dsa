from typing import Self

from pydantic import computed_field

from .._base import BaseSchema_


class BaseInput_(BaseSchema_):
    seed: float | int = 42

    @computed_field
    @property
    def seed_(self: Self, /) -> float | int:
        return self.seed
