from typing import Callable

from gradio import (
    Accordion,
    Blocks,
    Button,
    Dropdown,
    Image,
    Markdown,
    Number,
    Row,
    Text,
)

from ..components import WordCloudPage


def build_subapp(
    ui: WordCloudPage,
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
                    ignore_words: Text = Text(
                        **ui.text_ignore_words.dump(),
                    )
                    background_color_mode: Dropdown = Dropdown(
                        **ui.dropdown_background_color_mode.dump(),
                    )
                    colormap: Dropdown = Dropdown(
                        **ui.dropdown_colormap.dump(),
                    )
                    colormode: Dropdown = Dropdown(
                        **ui.dropdown_colormode.dump(),
                    )

                with Row():
                    max_words: Number = Number(
                        **ui.number_max_words.dump(),
                    )
                    max_fontsize: Number = Number(
                        **ui.number_max_fontsize.dump(),
                    )
                    plot_width: Number = Number(
                        **ui.number_width.dump(),
                    )
                    plot_height: Number = Number(
                        **ui.number_height.dump(),
                    )

            btn_create: Button = Button(
                **ui.btn_create.dump(),
            )

            image_wordcloud: Image = Image(
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
                    ignore_words,
                    background_color_mode,
                    colormap,
                    colormode,
                    max_words,
                    max_fontsize,
                    plot_width,
                    plot_height,
                ],
                outputs=image_wordcloud,
            )

            gui.load(
                fn=on_load,
                outputs=dropdown_year,
            )

        return gui

    return _fn
