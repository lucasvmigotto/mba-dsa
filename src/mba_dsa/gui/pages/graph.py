from typing import Callable

from gradio import (
    HTML,
    Accordion,
    Blocks,
    Button,
    Checkbox,
    Dropdown,
    Markdown,
    Number,
    Row,
)

from ..components import GraphPage


def build_subapp(
    ui: GraphPage,
    /,
    on_load: Callable,
    on_btn_create_callback: Callable,
) -> Callable[[Blocks], Blocks]:
    def _fn(gui: Blocks, /):
        with gui.route(*ui.route_):
            Markdown(**ui.md_title.dump())

            dropdown_year: Dropdown = Dropdown(
                **ui.dropdown_year_filter.dump(),
            )

            with Accordion(**ui.accordion_tf_idf.dump()):
                with Row():
                    tfidf_features: Number = Number(
                        **ui.number_features.dump(),
                    )
                    tfidf_score_limit: Number = Number(
                        **ui.number_score_limit.dump(),
                    )
                    tfidf_score_threshold: Number = Number(
                        **ui.number_score_threshold.dump(),
                    )
                    tfidf_score_sort: Dropdown = Dropdown(
                        **ui.dropdown_sort.dump(),
                    )
                with Row():
                    tfidf_min_df: Number = Number(
                        **ui.number_min_df.dump(),
                    )
                    tfidf_max_df: Number = Number(
                        **ui.number_max_df.dump(),
                    )
                    tfidf_min_ngram: Number = Number(
                        **ui.number_min_ngram.dump(),
                    )
                    tfidf_max_ngram: Number = Number(
                        **ui.number_max_ngram.dump(),
                    )

            with Accordion(**ui.accordion_preferences.dump()):
                with Row():
                    directional: Checkbox = Checkbox(
                        **ui.checkbox_directional.dump(),
                    )
                    nodes_distance: Number = Number(
                        **ui.number_nodes_distance.dump(),
                    )
                    spring_length: Number = Number(
                        **ui.number_spring_layout.dump(),
                    )

                with Row():
                    width_value: Number = Number(
                        **ui.number_width.dump(),
                    )
                    width_unit: Dropdown = Dropdown(
                        **ui.dropdown_width.dump(),
                    )
                    height_value: Number = Number(
                        **ui.number_height.dump(),
                    )
                    height_unit: Dropdown = Dropdown(
                        **ui.dropdown_height.dump(),
                    )

            btn_create: Button = Button(
                **ui.btn_create.dump(),
            )

            html_graph: HTML = HTML(
                label=str(ui.title.emoji_text),
            )

            btn_create.click(
                fn=on_btn_create_callback,
                inputs=[
                    dropdown_year,
                    tfidf_features,
                    tfidf_score_limit,
                    tfidf_score_threshold,
                    tfidf_score_sort,
                    tfidf_min_df,
                    tfidf_max_df,
                    tfidf_min_ngram,
                    tfidf_max_ngram,
                    directional,
                    nodes_distance,
                    spring_length,
                    width_value,
                    width_unit,
                    height_value,
                    height_unit,
                ],
                outputs=html_graph,
            )

            gui.load(
                fn=on_load,
                outputs=dropdown_year,
            )

        return gui

    return _fn
