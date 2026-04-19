from typing import Sequence

from gradio import (
    Accordion,
    Blocks,
    Button,
    Dropdown,
    Image,
    Markdown,
    Number,
    Row,
    Slider,
    Text,
)

from ..schemas import WordCloudInputs
from ..schemas._types import OnWordCloudCallback, SubAppBuilder
from ..settings.ui import WordCloudUISettings


def build_sub_app(
    settings: WordCloudUISettings,
    years_sequence: Sequence[str],
    on_btn_callback_fn: OnWordCloudCallback,
    /,
) -> SubAppBuilder:
    def _fn(gui: Blocks, /) -> Blocks:
        with gui.route(*settings.navbar_props):
            Markdown(settings.title_md())

            years_dropdown = Dropdown(
                **settings.data_dpd_props,
                choices=years_sequence,
                value=years_sequence[0],
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
                with Row():
                    wordcloud_ignore = Text(
                        **settings.wordcloud_ignore_props,
                    )
                    wordcloud_background_color = Dropdown(
                        **settings.wordcloud_background_color_props,
                    )
                    wordcloud_colormap = Dropdown(
                        **settings.wordcloud_colormap_props,
                    )
                    wordcloud_colormode = Dropdown(
                        **settings.wordcloud_colormode_props,
                    )
                with Row():
                    wordcloud_max_words = Slider(
                        **settings.wordcloud_max_words_props,
                    )
                    wordcloud_max_fontsize = Number(
                        **settings.wordcloud_max_fontsize_props,
                    )
                    wordcloud_width = Number(
                        **settings.wordcloud_width_props,
                    )
                    wordcloud_height = Number(
                        **settings.wordcloud_height_props,
                    )

            btn_process = Button(
                **settings.pROCESS_DATA_btn_props,
            )

            with Row():
                wordcloud_image = Image()

            btn_process.click(
                on_btn_callback_fn(
                    WordCloudInputs(
                        vec_max_features=tf_idf_max_features.value,
                        vec_score_threshold=tf_idf_score_threshold.value,
                        vec_score_limit=tf_idf_score_limit.value,
                        vec_score_sort=tf_idf_score_sort.value,
                        ignore=wordcloud_ignore.value,
                        background_color=wordcloud_background_color.value,
                        colormap=wordcloud_colormap.value,
                        colormode=wordcloud_colormode.value,
                        max_words=wordcloud_max_words.value,
                        max_fontsize=wordcloud_max_fontsize.value,
                        width=wordcloud_width.value,
                        height=wordcloud_height.value,
                    )
                ),
                inputs=[years_dropdown],
                outputs=[wordcloud_image],
            )

        return gui

    return _fn
