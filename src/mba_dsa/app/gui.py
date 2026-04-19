from gradio import (
    Blocks,
    Markdown,
)

from ..schemas._types import SubAppBuilder
from ..settings.ui import MainUISettings


def build_gui(
    settings: MainUISettings,
    /,
    *apps: SubAppBuilder,
):
    with Blocks() as gui:
        Markdown(settings.title_md())

    for app in apps:
        app(gui).render()

    return gui
