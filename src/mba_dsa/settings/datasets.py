from ..schemas._types import DatasetSplitsType
from ._base import _BaseSettings


class DatasetsSettings(_BaseSettings):
    DATASET_ID: str = "lucasvmigotto/articles-g1-links"
    SPLIT: DatasetSplitsType = "train"

    BATCHED_DOWNLOAD: bool = True
