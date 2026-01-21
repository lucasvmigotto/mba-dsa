from PIL.Image import Image
from polars import LazyFrame

from mba_dsa.data import (
    build_graph,
    init_nodes,
    tf_idf,
    tf_idf_score,
)
from mba_dsa.plot import generate_graph, generate_wordcloud
from mba_dsa.utils import corpus_from_dataframe, shard_by_year


def on_btn_fn_graph(lf: LazyFrame):
    def fn(
        year: str,
        tf_idf_max_features: int,
        tf_idf_score_threshold: int,
        tf_idf_score_limit: int,
        tf_idf_score_sort: str,
        graph_nodes_distance: int,
        graph_spring_length: int,
        graph_width_value: int,
        graph_width_unit: str,
        graph_height_value: int,
        graph_height_unit: str,
    ) -> str:
        features, tfidf_vectorizer = tf_idf(
            shard_by_year(lf, year),
            column_name="lemmas",
            max_features=tf_idf_max_features,
        )
        return generate_graph(
            build_graph(
                init_nodes(
                    tf_idf_score(
                        features,
                        tfidf_vectorizer.get_feature_names_out(),
                        limit=tf_idf_score_limit,
                        threshold=tf_idf_score_threshold,
                        sort_order=tf_idf_score_sort,
                    ),
                    column_name="word",
                ),
                directional=True,
            ),
            width_unit=graph_width_unit,
            width_value=graph_width_value,
            height_value=graph_height_value,
            height_unit=graph_height_unit,
            node_distance=graph_nodes_distance,
            spring_length=graph_spring_length,
            wrap_in_iframe=True,
        )

    return fn


def on_btn_fn_wordcloud(lf: LazyFrame):
    def fn(
        year: str,
        wordcloud_ignore: str,
        wordcloud_background_color: str,
        wordcloud_colormap: str,
        wordcloud_colormode: str,
        wordcloud_max_words: int,
        wordcloud_max_fontsize: int,
        wordcloud_width: int,
        wordcloud_height: int,
        wordcloud_seed: int,
    ) -> Image:
        return generate_wordcloud(
            corpus_from_dataframe(shard_by_year(lf, year), "lemmas"),
            ignore=[word.strip() for word in wordcloud_ignore.split(",")]
            if wordcloud_ignore
            else None,
            background_color=wordcloud_background_color,
            colormap=wordcloud_colormap,
            mode=wordcloud_colormode,
            max_words=wordcloud_max_words,
            max_font_size=wordcloud_max_fontsize,
            width=wordcloud_width,
            height=wordcloud_height,
            seed=wordcloud_seed,
        )

    return fn


def on_btn_fn_vectorize(lf: LazyFrame):
    def fn(
        year: str,
        tf_idf_max_features: int,
        tf_idf_score_threshold: int,
        tf_idf_score_limit: int,
        tf_idf_score_sort: str,
        graph_nodes_distance: int,
        graph_spring_length: int,
        graph_width_value: int,
        graph_width_unit: str,
        graph_height_value: int,
        graph_height_unit: str,
        wordcloud_ignore: str,
        wordcloud_background_color: str,
        wordcloud_colormap: str,
        wordcloud_colormode: str,
        wordcloud_max_words: int,
        wordcloud_max_fontsize: int,
        wordcloud_width: int,
        wordcloud_height: int,
        wordcloud_seed: int,
    ) -> tuple[str, Image]:
        return on_btn_fn_graph(lf)(
            year,
            tf_idf_max_features,
            tf_idf_score_threshold,
            tf_idf_score_limit,
            tf_idf_score_sort,
            graph_nodes_distance,
            graph_spring_length,
            graph_width_value,
            graph_width_unit,
            graph_height_value,
            graph_height_unit,
        ), on_btn_fn_wordcloud(lf)(
            year,
            wordcloud_ignore,
            wordcloud_background_color,
            wordcloud_colormap,
            wordcloud_colormode,
            wordcloud_max_words,
            wordcloud_max_fontsize,
            wordcloud_width,
            wordcloud_height,
            wordcloud_seed,
        )

    return fn
