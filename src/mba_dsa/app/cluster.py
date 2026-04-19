from typing import Sequence

from gradio import (
    Accordion,
    Blocks,
    Button,
    Dropdown,
    Image,
    Markdown,
    Number,
    Plot,
    Row,
    Tab,
)

from ..schemas import ClusterInputs
from ..schemas._types import OnClusterCallback, SubAppBuilder
from ..settings.ui import ClusterUISettings


def build_sub_app(
    settings: ClusterUISettings,
    years_sequence: Sequence[str],
    on_btn_callback_fn: OnClusterCallback,
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
                with Row():
                    ngram_range = Number(
                        **settings.ngram_range_props,
                    )

                    min_df = Number(
                        **settings.min_df_props,
                    )

                    max_df = Number(
                        **settings.max_df_props,
                    )

                with Row():
                    pca_n_components = Number(
                        **settings.pca_n_components_props,
                    )

                    kmeans_n_clusters = Number(
                        **settings.kmeans_n_clusters_props,
                    )

                with Row():
                    random_state = Number(
                        **settings.random_state_props,
                    )

                    random_state_pca = Number(
                        **settings.random_state_pca_props,
                    )

                    random_state_kmeans = Number(
                        **settings.random_state_kmeans_props,
                    )

            btn_process = Button(**settings.process_data_btn_props)

            with Tab(label=settings.tab_2d_label):
                plot_2d = Image(label=settings.tab_2d_label)

            with Tab(label=settings.tab_3d_label):
                plot_3d = Plot(label=settings.tab_3d_label)

            btn_process.click(
                on_btn_callback_fn(
                    ClusterInputs(
                        ngram_range=ngram_range.value,
                        min_df=min_df.value,
                        max_df=max_df.value,
                        pca_n_components=pca_n_components.value,
                        kmeans_n_clusters=kmeans_n_clusters.value,
                        random_state=random_state.value,
                        random_state_pca=random_state_pca.value,
                        random_state_kmeans=random_state_kmeans.value,
                    )
                ),
                inputs=[years_dropdown],
                outputs=[plot_2d, plot_3d],
            )

        return gui

    return _fn
