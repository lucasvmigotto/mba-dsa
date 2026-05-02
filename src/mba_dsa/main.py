def main() -> None:
    from .gui.callbacks import ClusterCallback, GraphCallback, WordCloudCallback
    from .gui.components import (
        ClusterPage,
        GraphPage,
        MainPage,
        WordCloudPage,
    )
    from .gui.pages import build_app, build_cluster, build_graph, build_wordcloud
    from .settings import Settings
    from .utils import load_data, setup_envvars, setup_log

    settings = Settings()

    setup_envvars(settings.GRADIO.env, settings.HF.env)
    setup_log(settings.LOG)

    lf = load_data(settings.DATASETS)
    graph, wordcloud, cluster = (
        GraphCallback(lf),
        WordCloudCallback(lf),
        ClusterCallback(lf),
    )

    build_app(
        MainPage(),
        build_graph(
            GraphPage(),
            on_load=graph.on_load_async,
            on_btn_create_callback=graph.on_btn_create_callback_async,
        ),
        build_wordcloud(
            WordCloudPage(),
            on_load=wordcloud.on_load_async,
            on_btn_create_callback=wordcloud.on_btn_create_callback_async,
        ),
        build_cluster(
            ClusterPage(),
            on_load=cluster.on_load_async,
            on_btn_create_callback=cluster.on_btn_create_callback_async,
        ),
    ).launch(**settings.GRADIO.config)
