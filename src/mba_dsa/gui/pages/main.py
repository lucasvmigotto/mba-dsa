from typing import Callable, Optional

from gradio import Blocks, Markdown

from ..components.main import MainPage


def build_app(
    ui: MainPage,
    /,
    *apps: Callable[[Blocks], Blocks],
    on_load: Optional[Callable] = None,
) -> Blocks:
    with Blocks(title=str(ui.title)) as gui:
        Markdown(**ui.md_title.dump())

        if on_load:
            gui.load(fn=on_load)

    for app in apps:
        app(gui).render()

    return gui
