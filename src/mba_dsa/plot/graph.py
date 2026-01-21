from typing import Literal

from networkx import DiGraph, Graph
from pyvis.network import Network


def iframe_wrapper(
    html: str,
    /,
    width_value: float | int | None = 100,
    width_unit: Literal["%", "px"] | None = "%",
    height_value: float | int | None = 700,
    height_unit: Literal["%", "px"] | None = "px",
) -> str:
    return f"""
        <iframe
            style="width: {width_value}{width_unit};height: {height_value}{height_unit};margin:0 auto;"
            allow="midi;geolocation;microphone;camera;display-capture;encrypted-media;"
            sandbox="allow-modals allow-forms allow-scripts allow-same-origin allow-popups allow-top-navigation-by-user-activation allow-downloads"
            allowfullscreen=""
            allowpaymentrequest=""
            frameborder="0"
            srcdoc='{html.replace("'", '"')}'>
        </iframe>
    """


def generate_graph(
    graph: Graph | DiGraph,
    /,
    width_value: float | int | None = 100,
    width_unit: Literal["%", "px"] | None = "%",
    height_value: float | int | None = 700,
    height_unit: Literal["%", "px"] | None = "px",
    cdn_resources: Literal["in_line", "local", "remote"] | None = "remote",
    node_distance: int | None = 75,
    spring_length: int | None = 75,
    wrap_in_iframe: bool | None = False,
) -> str:
    plot = Network(
        cdn_resources=cdn_resources,
        width=f"{width_value}{width_unit}",
        height=f"{height_value}{height_unit}",
        directed=isinstance(graph, DiGraph),
    )

    for node in graph.nodes:
        plot.add_node(node)
    for node_1, node_2 in graph.edges:
        plot.add_edge(node_1, node_2)

    plot.repulsion(
        node_distance=node_distance,
        spring_length=spring_length,
    )

    return (
        iframe_wrapper(
            plot.generate_html(),
            width_value=width_value,
            width_unit=width_unit,
            height_value=height_value,
            height_unit=height_unit,
        )
        if wrap_in_iframe
        else plot.generate_html()
    )
