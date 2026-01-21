from typing import Callable, Sequence

from gradio import (
    HTML,
    Accordion,
    Blocks,
    Button,
    Column,
    Dropdown,
    Image,
    Number,
    Row,
    Slider,
    Tab,
    Text,
)


def build_gui(
    years_dropdown_values: Sequence[str],
    on_btn_fn_vectorize: Callable,
    on_btn_fn_graph: Callable,
    on_btn_fn_wordcloud: Callable,
):
    with Blocks() as demo:
        with Row():
            dropdown_year = Dropdown(
                choices=years_dropdown_values,
                label="Select a year to filter the results",
                value=years_dropdown_values[0],
                interactive=True,
                scale=5,
            )
            btn_vectorizer = Button(
                value="Vectorize data",
                scale=5,
            )

        with Tab(label="Graph Network"):
            with Row():
                with Accordion(label="Graph network preferences", open=False):
                    with Row():
                        tf_idf_max_features = Slider(
                            label="TF-IDF Vectorizer features",
                            minimum=1_000,
                            maximum=20_000,
                            value=10_000,
                            step=1_000,
                            interactive=True,
                        )
                        tf_idf_score_threshold = Number(
                            label="Threshold value for TF-IDF score",
                            minimum=0,
                            maximum=1_000,
                            value=100,
                            precision=1,
                            step=10,
                            interactive=True,
                        )
                        tf_idf_score_limit = Number(
                            label="Limit up to N results from TF-IDF score",
                            minimum=0,
                            value=1000,
                            precision=1,
                            step=10,
                            interactive=True,
                        )
                        tf_idf_score_sort = Dropdown(
                            choices=[("Ascending", "ascd"), ("Descending", "desc")],
                            label="Sort order for TF-IDF scores",
                            value="desc",
                            interactive=True,
                        )
                    with Row():
                        with Column():
                            graph_nodes_distance = Number(
                                label="Distance between nodes",
                                minimum=0,
                                value=75,
                                precision=1,
                                step=5,
                                interactive=True,
                            )
                            graph_spring_length = Number(
                                label="Spring length",
                                minimum=0,
                                value=75,
                                precision=1,
                                step=5,
                                interactive=True,
                            )
                        with Column():
                            with Row():
                                graph_width_value = Number(
                                    label="Width Value",
                                    minimum=100,
                                    value=100,
                                    step=10,
                                    interactive=True,
                                    scale=5,
                                )
                                graph_width_unit = Dropdown(
                                    choices=[("Percentage", "%"), ("Pixels", "px")],
                                    label="Width unit",
                                    value="%",
                                    interactive=True,
                                )

                            with Row():
                                graph_height_value = Number(
                                    label="Height Value",
                                    minimum=100,
                                    value=700,
                                    step=10,
                                    interactive=True,
                                    scale=5,
                                )
                                graph_height_unit = Dropdown(
                                    choices=[("Percentage", "%"), ("Pixels", "px")],
                                    label="Height unit",
                                    value="px",
                                    interactive=True,
                                )

                    btn_graph = Button(
                        value="Regenerate graph network",
                        scale=5,
                    )

            with Row():
                graph_plot = HTML()

        with Tab(label="Word Cloud"):
            with Accordion(label="Word cloud preferences", open=False):
                with Row():
                    wordcloud_ignore = Text(
                        label="Ignore words",
                        placeholder="foo, bar, baz, ...",
                        value=None,
                        interactive=True,
                    )
                    wordcloud_background_color = Dropdown(
                        choices=[("Dark", "dark"), ("White", "white")],
                        label="Background color",
                        value="white",
                        interactive=True,
                    )
                    wordcloud_colormap = Dropdown(
                        choices=[("Tab 10", "tab10"), ("Viridis", "viridis")],
                        label="Font color map",
                        value="tab10",
                        interactive=True,
                    )
                    wordcloud_colormode = Dropdown(
                        choices=["RGB", "RGBA"],
                        label="Color mode",
                        value="RGB",
                        interactive=True,
                    )
                with Row():
                    wordcloud_max_words = Slider(
                        label="Max words",
                        minimum=100,
                        maximum=1_000,
                        value=200,
                        step=10,
                        interactive=True,
                    )
                    wordcloud_max_fontsize = Number(
                        label="Max font size",
                        minimum=10,
                        value=100,
                        interactive=True,
                    )
                    wordcloud_width = Number(
                        label="Plot width",
                        minimum=100,
                        value=800,
                        interactive=True,
                    )
                    wordcloud_height = Number(
                        label="Plot height",
                        minimum=100,
                        value=800,
                        interactive=True,
                    )

                    wordcloud_seed = Number(
                        label="Seed",
                        minimum=0,
                        value=42,
                        interactive=True,
                    )
                btn_wordcloud = Button(
                    value="Regenerate wordcloud",
                    scale=5,
                )

            with Row():
                wordcloud_image = Image()

        TFIDF_INPUTS = [
            tf_idf_max_features,
            tf_idf_score_threshold,
            tf_idf_score_limit,
            tf_idf_score_sort,
        ]
        GRAPH_INPUTS = [
            graph_nodes_distance,
            graph_spring_length,
            graph_width_value,
            graph_width_unit,
            graph_height_value,
            graph_height_unit,
        ]
        WORDCLOUD_INPUTS = [
            wordcloud_ignore,
            wordcloud_background_color,
            wordcloud_colormap,
            wordcloud_colormode,
            wordcloud_max_words,
            wordcloud_max_fontsize,
            wordcloud_width,
            wordcloud_height,
            wordcloud_seed,
        ]
        btn_vectorizer.click(
            on_btn_fn_vectorize,
            inputs=[dropdown_year, *TFIDF_INPUTS, *GRAPH_INPUTS, *WORDCLOUD_INPUTS],
            outputs=[graph_plot, wordcloud_image],
        )
        btn_graph.click(
            on_btn_fn_graph,
            inputs=[dropdown_year, *TFIDF_INPUTS, *GRAPH_INPUTS],
            outputs=[graph_plot],
        )
        btn_wordcloud.click(
            on_btn_fn_wordcloud,
            inputs=[dropdown_year, *WORDCLOUD_INPUTS],
            outputs=[wordcloud_image],
        )

    return demo
