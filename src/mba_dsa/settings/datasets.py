from typing import Literal

from pydantic import BaseModel


class DatasetsSettings(BaseModel):
    DATASET_ID: str = "lucasvmigotto/articles-g1-links"
    SPLIT: Literal["train"] = "train"

    BATCHED_DOWNLOAD: bool = True
