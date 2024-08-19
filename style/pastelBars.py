import matplotlib as mpl
from matplotlib import cycler


def pastel(bar: bool = False) -> dict:
    pastel_style = {
        "axes.prop_cycle": cycler('color', ["#FDABAB", "#FFD7A6", "#F7FAB2", "#C6F8BD", "#95F1FA", "#9BBFF8", "#FAC1FA"]),
        "figure.facecolor": "#E4EAF2",
        "axes.facecolor": "#E4EAF2",
        "savefig.facecolor": "#E4EAF2",
        "axes.edgecolor": "#736048",
        "axes.linewidth": 1.2,
        "grid.color": "#736048",
        "lines.linewidth": 2.2,
        "font.family": "monospace",
        "text.color": "#736048",
        "axes.labelcolor": "#736048",
        "xtick.color": "#736048",
        "ytick.color": "#736048",
    }

    if bar:
        pastel_style["font.size"] = 13
        # hide xticks for bars; the label is enough
        pastel_style["xtick.major.width"] = 0
        # Hide yticks and labels
        pastel_style["ytick.major.width"] = 0
        pastel_style["ytick.labelleft"] = False
        # Remove all frame lines
        for i in ["bottom","left","right","top"]:
            pastel_style[f"axes.spines.{i}"] = False
    return pastel_style

