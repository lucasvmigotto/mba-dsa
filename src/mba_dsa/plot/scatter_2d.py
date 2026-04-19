from typing import Collection, Sequence

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.pyplot import subplots
from polars import DataFrame

from ._utils import _PALETTE

_SPINES_TO_HIDE: Collection[str] = {"top", "bottom", "left", "right"}


def plot_scatter_2d(
    df: DataFrame,
    col_x: str,
    col_y: str,
    col_clusters: str,
    /,
    palette: Sequence[str] | None = None,
    spines_to_hide: Collection[str] = _SPINES_TO_HIDE,
    plot_size: tuple[int, int] = (15, 6),
    yaxis_is_visible: bool = True,
    xaxis_is_visible: bool = True,
    plot_title: str | None = None,
) -> tuple[Figure, Axes]:
    fig, ax = subplots(figsize=plot_size)
    _palette = (palette or _PALETTE)[
        : len(
            (clusters := df.get_column(col_clusters)).unique(),
        )
    ]

    ax.scatter(
        df.get_column(col_x),
        df.get_column(col_y),
        c=[_palette[i] for i in clusters],
    )

    ax.xaxis.set_visible(xaxis_is_visible)
    ax.yaxis.set_visible(yaxis_is_visible)

    for s in spines_to_hide:
        ax.spines[s].set_visible(False)

    if plot_title:
        ax.set_title(plot_title)

    return fig, ax
