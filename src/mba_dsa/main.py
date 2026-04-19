from typing import Sequence


def main() -> None:
    from .app import build_gui, build_sub_app_graph, build_sub_app_wordcloud
    from .data import clean_dataframe, load_data, unique
    from .services import GraphCallback, WordCloudCallback
    from .settings import Settings
    from .utils import setup_envvars, setup_log

    settings = Settings()

    setup_envvars(settings.GRADIO.env, settings.HF.env)
    setup_log(settings.LOG)

    lf = load_data(
        settings.DATASETS,
        return_lazy=True,
    ).pipe(clean_dataframe, "lemmas")

    years_sequence: Sequence[str] = unique(lf, "year")

    demo = build_gui(
        settings.UI_MAIN,
        build_sub_app_graph(
            settings.UI_GRAPH,
            years_sequence,
            GraphCallback(settings).on_callback(lf),
        ),
        build_sub_app_wordcloud(
            settings.UI_WORDCLOUD,
            years_sequence,
            WordCloudCallback(settings).on_callback(lf),
        ),
    )

    demo.launch(**settings.GRADIO.config)
