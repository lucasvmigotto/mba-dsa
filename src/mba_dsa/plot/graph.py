from typing import Self, Type

from networkx import DiGraph, Graph
from pyvis.network import Network

from ..schemas.inputs import GraphInputs
from ._base import PlotterBase_


class GraphPlotter(PlotterBase_):
    @classmethod
    def iframe_wrapper(cls: Type[Self], html: str, /, inputs: GraphInputs) -> str:
        return f"""
            <iframe
                style="width: {inputs.width_display};height: {inputs.height_display};margin:0 auto;"
                allow="midi;geolocation;microphone;camera;display-capture;encrypted-media;"
                sandbox="allow-modals allow-forms allow-scripts allow-same-origin allow-popups allow-top-navigation-by-user-activation allow-downloads"
                allowfullscreen=""
                allowpaymentrequest=""
                frameborder="0"
                srcdoc='{html.replace("'", '"')}'>
            </iframe>
        """

    def graph(
        self: Self,
        graph: Graph | DiGraph,
        /,
        *args,
        **kwargs,
    ) -> str:
        inputs = GraphInputs(**kwargs)
        plot = Network(
            cdn_resources="in_line",
            width=inputs.width_display,
            height=inputs.height_display,
            directed=isinstance(graph, DiGraph),
        )

        for node in graph.nodes:
            plot.add_node(node)
        for node_1, node_2 in graph.edges:
            plot.add_edge(node_1, node_2)

        plot.repulsion(
            node_distance=inputs.nodes_distance,
            spring_length=inputs.spring_length,
        )

        return self.iframe_wrapper(
            plot.generate_html(),
            inputs=inputs,
        )
