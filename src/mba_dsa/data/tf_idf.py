from numpy import ndarray
from polars import DataFrame, LazyFrame, Series, col
from scipy.sparse._csr import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

from ..schemas._types import PolarsData
from ..settings.ui._commons import SortOrderChoiceSignType
from ..utils.data import polars_to_sequence
from ..utils.decorators import timeit


@timeit
def tf_idf(
    corpus: PolarsData,
    /,
    max_features: int | None = 10_000,
    ngram_range: tuple[int, int] | None = (2, 2),
    min_df: float | int | None = 1,
    max_df: float | int | None = 1.0,
    column_name: str | None = None,
    **tf_idf_kwargs,
) -> tuple[csr_matrix, TfidfVectorizer]:
    _corpus = (
        polars_to_sequence(corpus, column_name)
        if isinstance(corpus, (LazyFrame, DataFrame, Series))
        else corpus
    )

    vec = TfidfVectorizer(
        ngram_range=ngram_range,
        max_features=max_features,
        min_df=min_df,
        max_df=max_df,
        **tf_idf_kwargs,
    )

    return vec.fit_transform(_corpus), vec


@timeit
def tf_idf_score(
    features: csr_matrix,
    features_names: ndarray,
    /,
    limit: int | None = None,
    sort_order: SortOrderChoiceSignType | None = "desc",
    threshold: float | None = None,
) -> DataFrame:
    df = (
        DataFrame(
            {
                "word": features_names,
                "score": features.sum(axis=0).A1,
            },
        )
        .sort(by="score", descending=sort_order == "desc")
        .limit(limit or 100)
    )

    if threshold:
        return df.filter(col("score") > threshold)

    return df
