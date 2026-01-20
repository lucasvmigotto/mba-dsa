from pydantic_settings import BaseSettings, SettingsConfigDict

from .datasets import DatasetsSettings
from .gradio import GradioSettings
from .log import LogSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_ignore_empty=True,
        extra="ignore",
        env_prefix="MBA_DSA__",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    GRADIO: GradioSettings = GradioSettings()
    DATASETS: DatasetsSettings = DatasetsSettings()
    LOG: LogSettings = LogSettings()
