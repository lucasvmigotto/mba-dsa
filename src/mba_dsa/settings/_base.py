from typing import Any, Self

from pydantic import BaseModel, ConfigDict, computed_field


class _BaseSettings(BaseModel):
    model_config: ConfigDict = ConfigDict(
        use_enum_values=True,
        validate_by_name=True,
        extra="ignore",
        frozen=True,
    )

    @computed_field
    @property
    def config(self: Self) -> dict[str, Any]:
        return {}

    @computed_field
    @property
    def env(self: Self) -> dict[str, str]:
        return {}
