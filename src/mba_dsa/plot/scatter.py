from typing import Collection, Sequence

import plotly.graph_objects as go
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.pyplot import subplots
from polars import DataFrame

from ._utils import _PALETTE


def plot_cluster_2d(
    df: DataFrame,
    col_x: str,
    col_y: str,
    col_clusters: str,
    /,
    palette: Sequence[str] | None = None,
    spines_to_hide: Collection[str] = {},
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


def plot_cluster_3d(
    df: DataFrame,
    col_x: str,
    col_y: str,
    col_z: str,
    col_clusters: str,
    /,
    palette: Sequence[str] | None = None,
):
    _palette = (palette or _PALETTE)[
        : len(
            (clusters := df.get_column(col_clusters)).unique(),
        )
    ]
    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=df.get_column(col_x),
                y=df.get_column(col_y),
                z=df.get_column(col_z),
                mode="markers",
                marker={
                    "size": 5,
                    "color": [_palette[i] for i in clusters],
                    "opacity": 0.8,
                },
                customdata=df.select("year", "month", "lemmas"),
                hovertemplate=(
                    "%{customdata[1]:02}/%{customdata[0]}\n%{customdata[2]}"
                ),
            )
        ]
    )

    return fig
