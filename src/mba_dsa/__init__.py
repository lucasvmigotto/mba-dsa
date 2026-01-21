from .app import build_gui, on_btn_fn_graph, on_btn_fn_vectorize, on_btn_fn_wordcloud
from .data import clean_dataframe, load_data, unique
from .settings import Settings
from .utils import setup_envvars, setup_log


def main() -> None:
    settings = Settings()

    setup_envvars(settings.GRADIO.env, settings.HF.env)
    setup_log(settings.LOG)

    lf = load_data(return_lazy=True).pipe(clean_dataframe, "lemmas")

    demo = build_gui(
        unique(lf, column_name="year"),
        on_btn_fn_vectorize=on_btn_fn_vectorize(lf),
        on_btn_fn_graph=on_btn_fn_graph(lf),
        on_btn_fn_wordcloud=on_btn_fn_wordcloud(lf),
    )

    demo.launch(**settings.GRADIO.config)


if __name__ == "__main__":
    main()
