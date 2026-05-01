from logging import basicConfig, getLogger
from os import environ, getenv
from typing import Optional

from datasets.load import load_dataset
from polars import DataFrame, LazyFrame, concat

from ..settings import DatasetsSettings, LogSettings


def setup_log(settings: LogSettings | None = None):
    _settings: LogSettings = settings or LogSettings()
    basicConfig(**_settings.config)
    for mod, level in _settings.SUPPRESS_MODULES:
        getLogger(mod).setLevel(level or _settings.SUPPRESS_LEVEL)


def setup_envvars(*envs: dict[str, str]) -> None:
    for env in envs:
        for env_key, env_value in env.items():
            if not getenv(env_key):
                environ[env_key] = env_value


def load_data(
    settings: Optional[DatasetsSettings] = None, /, lazy: bool = True
) -> DataFrame | LazyFrame:
    _settings = settings or DatasetsSettings()
    return concat(
        [
            df.lazy() if lazy else df  # type: ignore
            for df in load_dataset(
                _settings.DATASET_ID, split=_settings.SPLIT
            ).to_polars(batched=_settings.BATCHED_DOWNLOAD)
        ]
    )
