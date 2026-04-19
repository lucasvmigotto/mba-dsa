from pathlib import Path
from typing import Self

from pydantic import DirectoryPath, computed_field

from ._base import _BaseSettings


class HuggingFaceSettings(_BaseSettings):
    HOME: DirectoryPath = Path("/tmp/.hf")

    @computed_field
    @property
    def env(self: Self) -> dict[str, str]:
        return {
            "HF_HOME": str(self.HOME),
        }
