from typing import TYPE_CHECKING, Any, Callable

from gradio import Blocks
from PIL.Image import Image

from ...settings.ui import UICommons
from .data import PolarsData

if TYPE_CHECKING:
    from ..inputs import GraphInputs, WordCloudInputs

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

type SubAppBuilder = Callable[[Blocks], Blocks]
type SubAppBuilderCaller = Callable[
    [
        UICommons,
        OnCallback,
    ],
    SubAppBuilder,
]
