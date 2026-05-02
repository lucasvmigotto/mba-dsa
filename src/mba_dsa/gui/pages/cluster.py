from typing import Callable

from gradio import (
    Accordion,
    Blocks,
    Button,
    Dropdown,
    Markdown,
    Number,
    Plot,
    Row,
)

from ..components import ClusterPage


def build_subapp(
    ui: ClusterPage,
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
                        **ui.number_score_threshold.dump()
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
                    pca_components: Number = Number(
                        **ui.number_pca_components.dump(),
                    )
                    pca_seed: Number = Number(
                        **ui.number_pca_seed.dump(),
                    )
                with Row():
                    kmeans_n_clusters: Number = Number(
                        **ui.number_kmeans_clusters.dump(),
                    )
                    kmeans_seed: Number = Number(
                        **ui.number_kmeans_seed.dump(),
                    )

            btn_create: Button = Button(
                **ui.btn_create.dump(),
            )

            plot_cluster: Plot = Plot(
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
                    pca_components,
                    pca_seed,
                    kmeans_n_clusters,
                    kmeans_seed,
                ],
                outputs=plot_cluster,
            )

            gui.load(
                fn=on_load,
                outputs=dropdown_year,
            )

        return gui

    return _fn
