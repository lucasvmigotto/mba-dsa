from typing import Literal

from ._base import BaseSettings_

type DatasetSplitsType_ = Literal["train", "test"]


class DatasetsSettings(BaseSettings_):
    DATASET_ID: str = "lucasvmigotto/articles-g1-links"
    SPLIT: DatasetSplitsType_ = "train"

    BATCHED_DOWNLOAD: bool = True
