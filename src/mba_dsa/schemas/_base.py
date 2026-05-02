from abc import ABC
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Collection,
    Optional,
    Self,
    Sequence,
    Type,
)

from polars import DataFrame, Enum, Float32, LazyFrame, Schema, Series, String, col
from pydantic import (
    AfterValidator,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    PositiveInt,
)
from scipy.sparse._csr import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

if TYPE_CHECKING:
    from .inputs import TFIDFInputs

type FilterByYearType = Annotated[
    int,
    Field(ge=2003, le=2025),
    AfterValidator(func=str),
]


class BaseSchema_(BaseModel, ABC):
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        extra="ignore",
        use_enum_values=True,
    )


class BaseDataEntry_(BaseSchema_, ABC):
    year: PositiveInt
    month: PositiveInt
    url: HttpUrl
    lemmas: str

    @classmethod
    def df_schema(cls: Type[Self], /) -> dict[str, Any]:
        return {
            "year": Enum(
                categories=map(str, range(2003, 2026)),
            ),
            "month": Enum(
                categories=map(str, range(1, 13)),
            ),
            "url": String,
            "lemmas": String,
        }

    @classmethod
    def polars_to_sequence(
        cls: Type[Self],
        corpus: LazyFrame | DataFrame | Series,
        /,
        col_name: Optional[str] = None,
    ) -> Sequence[str]:
        if isinstance(corpus, (LazyFrame, DataFrame)) and not col_name:
            raise ValueError(
                "When using polars LazyFrame or DataFrame,"
                " the `col_name` argument must be informed"
            )
        try:
            return {
                Series: lambda c: c.to_list(),
                DataFrame: lambda c: cls.polars_to_sequence(c.get_column(col_name)),
                LazyFrame: lambda c: cls.polars_to_sequence(
                    c.select(col_name).collect().get_column(col_name),
                    col_name,
                ),
            }[type(corpus)](corpus)  # ty:ignore[invalid-argument-type]
        except KeyError:
            raise ValueError(
                (
                    f"{type(corpus)} not supported, use polars"
                    " LazyFrame, DataFrame or Series instead"
                )
            )

    @classmethod
    def pipe_clean_lemmas(
        cls: Type[Self],
        pf: DataFrame,
        /,
        col_lemmas: str = "lemmas",
    ) -> DataFrame:
        return pf.with_columns(
            col(name=col_lemmas)
            .str.replace_all(r"\b\w{2}\b", "")
            .str.replace_all(r"\s+", " ")
            .str.strip_chars()
        )

    @classmethod
    def pipeline(
        cls: Type[Self],
        lf: LazyFrame,
        year: FilterByYearType,
        /,
        **kwargs,
    ) -> DataFrame:
        return DataFrame(
            data=lf.filter(
                col(name="year") == year,
            ),
            schema=Schema(cls.df_schema()),
        ).pipe(function=cls.pipe_clean_lemmas)

    @classmethod
    def vectorize(
        cls: Type[Self],
        data: Collection[str],
        /,
        options: Optional[TFIDFInputs] = None,
    ) -> tuple[csr_matrix, TfidfVectorizer]:
        options_: TFIDFInputs = options or TFIDFInputs()
        return (
            (
                vec := TfidfVectorizer(
                    ngram_range=options_.ngram_range,
                    max_features=options_.max_features,
                    min_df=options_.min_df,
                    max_df=options_.max_df,
                    sublinear_tf=options_.sublinear_tf,
                )
            ).fit_transform(data),
            vec,
        )

    @classmethod
    def features_from_vectors(
        cls: Type[Self],
        features: csr_matrix,
        vectorizer: TfidfVectorizer,
        /,
        options: Optional[TFIDFInputs] = None,
    ) -> DataFrame:
        options_: TFIDFInputs = options or TFIDFInputs()
        return (
            DataFrame(
                data={
                    "words": vectorizer.get_feature_names_out(),
                    "score": features.sum(axis=0).A1,
                },
                schema=Schema(
                    {
                        "words": tuple[String, String],
                        "score": Float32,
                    },
                ),
            )
            .sort(by="score", descending=options_.score_filter.is_descending)
            .limit(n=options_.score_limit)
            .filter(
                (col(name="score") > options_.score_threshold)
                if options_.score_threshold
                else True
            )
        )
