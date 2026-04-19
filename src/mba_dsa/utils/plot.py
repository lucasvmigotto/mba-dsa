from fontTools.misc.py23 import BytesIO
from matplotlib.figure import Figure
from PIL.Image import open as image_open
from PIL.ImageFile import ImageFile


def from_figure_to_image(
    fig: Figure,
    /,
    image_format: str = "png",
) -> ImageFile:
    fig.savefig((buffer := BytesIO()), format=image_format)
    buffer.seek(0)
    return image_open(buffer)
