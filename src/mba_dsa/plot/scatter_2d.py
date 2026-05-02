from typing import Self

from plotly.graph_objects import Figure, Scatter
from polars import DataFrame

from ._base import PlotterBase_


class Scatter2dPlotter(PlotterBase_):
    def plot(
        self: Self,
        df: DataFrame,
        /,
        *axes: str,
        **kwargs,
    ) -> Figure:
        col_x, col_y, *_ = axes
        col_clusters: str = kwargs["col_clusters"]
        _palette = self._palette[
            : len((clusters := df.get_column(col_clusters)).unique())
        ]
        (
            fig := Figure(
                data=[
                    Scatter(
                        x=df.get_column(col_x),
                        y=df.get_column(col_y),
                        mode="markers",
                        marker_color=[_palette[i] for i in clusters],
                        customdata=df.select("year", "month", "lemmas"),
                        hovertemplate=(
                            "%{customdata[2]}"
                            "<extra>%{customdata[1]:$.02d}"
                            "/%{customdata[0]}</extra>"
                        ),
                    )
                ]
            )
        ).update_layout(
            height=800,
        )

        fig.update_xaxes(
            showticklabels=False,
            ticks="",
            visible=False,
        )
        fig.update_yaxes(
            showticklabels=False,
            ticks="",
            visible=False,
        )

        return fig
