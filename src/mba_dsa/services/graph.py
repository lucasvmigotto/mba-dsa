from typing import Self

from ..data import build_graph, init_nodes, tf_idf, tf_idf_score
from ..plot import generate_graph
from ..schemas._types import (
    OnGraphCallback,
    OnGraphCallbackFn,
    PolarsData,
    PolarsDataFrames,
)
from ..schemas.inputs import GraphInputs
from ..utils import shard_by_year
from ._base import _BaseCallbackService


class GraphCallback(_BaseCallbackService):
    def on_load(
        self: Self,
        data: PolarsDataFrames,
        /,
        **kwargs,
    ):
        raise NotImplementedError()

    def on_callback(
        self: Self,
        data: PolarsData,
        /,
    ) -> OnGraphCallback:
        def _callback(props: GraphInputs, /) -> OnGraphCallbackFn:
            def _fn(year: int, /) -> str:
                features, tfidf_vectorizer = tf_idf(
                    shard_by_year(data, year),
                    column_name="lemmas",
                    max_features=props.vec_max_features,
                )
                return generate_graph(
                    build_graph(
                        init_nodes(
                            tf_idf_score(
                                features,
                                tfidf_vectorizer.get_feature_names_out(),
                                limit=props.vec_score_limit,
                                threshold=props.vec_score_threshold,
                                sort_order=props.vec_score_sort,
                            ),
                            column_name="word",
                        ),
                        directional=True,
                    ),
                    width_unit=props.width_unit,
                    width_value=props.width_value,
                    height_value=props.height_value,
                    height_unit=props.height_unit,
                    node_distance=props.nodes_distance,
                    spring_length=props.spring_length,
                    wrap_in_iframe=True,
                )

            return _fn

        return _callback
