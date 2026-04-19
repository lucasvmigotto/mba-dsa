from typing import Sequence

from gradio import (
    HTML,
    Accordion,
    Blocks,
    Button,
    Column,
    Dropdown,
    Markdown,
    Number,
    Row,
    Slider,
)

from ..schemas import GraphInputs
from ..schemas._types import OnGraphCallback, SubAppBuilder
from ..settings.ui import GraphUISettings


def build_sub_app(
    settings: GraphUISettings,
    years_sequence: Sequence[str],
    on_btn_callback_fn: OnGraphCallback,
    /,
) -> SubAppBuilder:
    def _fn(gui: Blocks, /) -> Blocks:
        with gui.route(*settings.navbar_props):
            Markdown(settings.title_md())

            years_dropdown = Dropdown(
                choices=years_sequence,
                value=years_sequence[0],
                **settings.data_dpd_props,
            )

            with Accordion(**settings.preferences_accordion_props):
                tf_idf_max_features = Slider(
                    **settings.tf_idf_max_features_props,
                )
                tf_idf_score_threshold = Number(
                    **settings.tf_idf_score_threshold_props,
                )
                tf_idf_score_limit = Number(
                    **settings.tf_idf_score_limit_props,
                )
                tf_idf_score_sort = Dropdown(
                    **settings.tf_idf_score_sort_props,
                )

            with Accordion(**settings.preferences_accordion_props):
                with Column():
                    graph_nodes_distance = Number(
                        **settings.graph_nodes_distance_props,
                    )
                    graph_spring_length = Number(
                        **settings.graph_spring_length_props,
                    )
                with Column():
                    with Row():
                        graph_width_value = Number(
                            **settings.graph_width_value_props,
                        )
                        graph_width_unit = Dropdown(
                            **settings.graph_width_unit_props,
                        )

                    with Row():
                        graph_height_value = Number(
                            **settings.graph_height_value_props,
                        )
                        graph_height_unit = Dropdown(
                            **settings.graph_height_unit_props,
                        )

            btn_process = Button(**settings.pROCESS_DATA_btn_props)

            with Row():
                graph_plot = HTML()

            btn_process.click(
                on_btn_callback_fn(
                    GraphInputs(
                        vec_max_features=tf_idf_max_features.value,
                        vec_score_threshold=tf_idf_score_threshold.value,
                        vec_score_limit=tf_idf_score_limit.value,
                        vec_score_sort=tf_idf_score_sort.value,
                        nodes_distance=graph_nodes_distance.value,
                        spring_length=graph_spring_length.value,
                        width_value=graph_width_value.value,
                        width_unit=graph_width_unit.value,
                        height_value=graph_height_value.value,
                        height_unit=graph_height_unit.value,
                    )
                ),
                inputs=[years_dropdown],
                outputs=[graph_plot],
            )

        return gui

    return _fn
