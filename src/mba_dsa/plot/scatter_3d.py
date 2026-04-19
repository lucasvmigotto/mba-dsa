from typing import Collection, Sequence

from plotly.graph_objects import Figure, Scatter3d
from polars import DataFrame

from ._utils import _PALETTE

_SPINES_TO_HIDE: Collection[str] = {"top", "bottom", "left", "right"}


def plot_scatter_3d(
    df: DataFrame,
    col_x: str,
    col_y: str,
    col_z: str,
    col_clusters: str,
    /,
    palette: Sequence[str] | None = None,
) -> Figure:
    _palette = (palette or _PALETTE)[
        : len(
            (clusters := df.get_column(col_clusters)).unique(),
        )
    ]
    fig = Figure(
        data=[
            Scatter3d(
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
