from typing import Sequence

from polars import DataFrame, LazyFrame, Series, col

from .decorators import timeit


@timeit
def polars_to_sequence(
    corpus: LazyFrame | DataFrame | Series, column_name: str | None = None
) -> Sequence[str]:
    if isinstance(corpus, (LazyFrame, DataFrame)) and not column_name:
        raise ValueError(
            "When using polars [LazyFrame|DataFrame|Series],"
            " the `column_name` argument must be informed"
        )
    try:
        return {
            Series: lambda c: c.to_list(),
            DataFrame: lambda c: polars_to_sequence(c.get_column(column_name)),
            LazyFrame: lambda c: polars_to_sequence(
                c.select(col(column_name)).collect().get_column(column_name),
                column_name,
            ),
        }[type(corpus)](corpus)
    except KeyError:
        raise ValueError(
            f"{type(corpus)} not supported, use polars LazyFrame, DataFrame or Series instead"
        )


@timeit
def shard_by_year(
    lf: LazyFrame,
    year: str | int,
    /,
    year_column_name: str = "year",
    lemmas_column_name: str = "lemmas",
) -> LazyFrame:
    return lf.filter(
        (
            col(year_column_name)
            if isinstance(year, str)
            else col(year_column_name).cast(int)
        )
        == year
    ).with_columns(
        col(lemmas_column_name)
        .str.replace_all(r"\b\w{2}\b", "")
        .str.replace_all(r"\s+", " ")
        .str.strip_chars()
        .alias(lemmas_column_name)
    )


@timeit
def corpus_from_dataframe(df: DataFrame | LazyFrame, column_name: str) -> str:
    _df: DataFrame = (
        df.select(column_name).collect()
        if isinstance(df, LazyFrame)
        else df.select(column_name)
    )

    return " ".join(_df.get_column(column_name).to_list())
