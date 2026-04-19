from typing import TYPE_CHECKING, Any, Callable

from gradio import Blocks
from matplotlib.axes import Axes
from matplotlib.figure import Figure as PltFigure
from PIL.Image import Image
from PIL.ImageFile import ImageFile
from plotly.graph_objects import Figure as PlotlyFigure

from ...settings.ui import UICommons
from .data import PolarsData

if TYPE_CHECKING:
    from ..inputs import ClusterInputs, GraphInputs, WordCloudInputs

type OnLoadCallback = Callable[[*Any], *Any]
type OnLoadCallbackCaller = Callable[[PolarsData], OnLoadCallback]
type OnCallback = Callable[
    [int, *Any],
    Any,
]

type OnGraphCallbackFn = Callable[[int], str]
type OnGraphCallback = Callable[
    [GraphInputs],
    OnGraphCallbackFn,
]
type OnGraphCallbackCaller = Callable[
    [PolarsData],
    OnGraphCallback,
]

type OnWordCloudCallbackFn = Callable[[int], Image]
type OnWordCloudCallback = Callable[
    [WordCloudInputs],
    OnWordCloudCallbackFn,
]
type OnWordCloudCallbackCaller = Callable[
    [PolarsData],
    OnWordCloudCallback,
]

type PltPlot = tuple[PltFigure, Axes]
type OnClusterCallbackReturn = tuple[ImageFile, PlotlyFigure | None]
type OnClusterCallbackFn = Callable[[int], OnClusterCallbackReturn]
type OnClusterCallback = Callable[
    [ClusterInputs],
    OnClusterCallbackFn,
]
type OnClusterCallbackCaller = Callable[
    [PolarsData],
    OnGraphCallback,
]

type SubAppBuilder = Callable[[Blocks], Blocks]
type SubAppBuilderCaller = Callable[
    [
        UICommons,
        OnCallback,
    ],
    SubAppBuilder,
]
