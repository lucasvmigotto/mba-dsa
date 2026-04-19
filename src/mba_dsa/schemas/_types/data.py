from polars import DataFrame, LazyFrame, Series

type PolarsDataFrames = DataFrame | LazyFrame
type PolarsData = PolarsDataFrames | Series
