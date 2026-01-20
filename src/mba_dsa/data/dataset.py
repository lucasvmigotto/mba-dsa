from typing import Sequence

from datasets import load_dataset
from polars import DataFrame, LazyFrame, col, concat

from ..settings import DatasetsSettings


def get_dataset(
    settings: DatasetsSettings | None = None, /, return_lazy: bool = True
) -> DataFrame | LazyFrame:
    _settings = settings or DatasetsSettings()
    return concat(
        [
            df.lazy() if return_lazy else df  # type: ignore
            for df in load_dataset(
                _settings.DATASET_ID, split=_settings.SPLIT
            ).to_polars(batched=_settings.BATCHED_DOWNLOAD)
        ]
    )


def clean_dataframe(
    df: DataFrame | LazyFrame, column_name: str
) -> DataFrame | LazyFrame:
    return df.with_columns(
        col(column_name)
        .str.replace_all(r"\b\w{2}\b", "")
        .str.replace_all(r"\s+", " ")
        .str.strip_chars()
        .alias(column_name)
    )


def unique(
    df: LazyFrame | DataFrame, /, column_name: str, sort_desc: bool = True
) -> Sequence[str]:
    unique_data: DataFrame | LazyFrame = (
        df.select(col(column_name)).unique().sort(by=column_name, descending=sort_desc)
    )  # type: ignore

    if isinstance(df, LazyFrame):
        unique_data: DataFrame = unique_data.collect()  # type: ignore

    return unique_data.get_column(column_name).to_list()
