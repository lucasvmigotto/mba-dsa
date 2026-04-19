from matplotlib.colors import to_hex
from matplotlib.pyplot import get_cmap

_PALETTE = list(map(to_hex, get_cmap("tab20")(range(20))))
