import numpy as np
import matplotlib as mpl
import itertools

MARKER = itertools.cycle(('o', 's', '^', '*', '>', '<', '8', 'p'))
LINES = itertools.cycle(("-", "--", ":", "-", "-."))


def figure_size(width_scale, height_scale=None, aspect=None, text_width=390):
    """Create a figure size tuple in inches from textwidth scale

    Args:
        width_scale (float): horizontal textwidth scale
        text_width (float, default=390pt): width of the text space in pt

    Returns:
        list: [horizontal, vertical] figsize in inches
    """
    fig_width_pt = text_width
    # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0 / 72.27
    # Convert pt to inch
    golden_mean = (np.sqrt(5.0) - 1.0) / 2.0
    # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt * inches_per_pt * width_scale

    if height_scale is None:
        # width_scale in inches
        fig_height = fig_width * golden_mean
    else:
        fig_height = fig_width * height_scale

    if aspect == 'equal':
        fig_size = [fig_width, fig_width]
    else:
        fig_size = [fig_width, fig_height]

    return fig_size


def use_config(typeface='Libertine'):
    """Update rc params for matplotlib """
    pgf_with_latex = {
        # # LaTeX default is 10pt font.
        "text.usetex": True,
        # # setup matplotlib to use latex for output
        "pgf.texsystem": "pdflatex",
        # use LaTeX to write all text
        "font.family": "serif",
        "font.serif": [],
        # # blank entries should cause plots to inherit fonts from the document
        # "font.sans-serif": [],
        # "font.monospace": [],
        'path.simplify': True,
        'path.simplify_threshold': 0.1,
        'legend.markerscale': .9,
        'legend.numpoints': 1,
        'legend.handlelength': 2,
        'legend.scatterpoints': 1,
        'legend.labelspacing': 0.5,
        'legend.facecolor': '#eff0f1',
        'legend.edgecolor': 'none',
        'legend.handletextpad': 0.5,  # pad between handle and text
        'legend.borderaxespad': 0.5,  # pad between legend and axes
        'legend.borderpad': 0.5,  # pad between legend and legend content
        'legend.columnspacing': 1,  # pad between each legend column
        'axes.spines.left': True,
        'axes.spines.top': True,
        'axes.titlesize': 'medium',
        'axes.spines.bottom': True,
        'axes.spines.right': True,
        'axes.axisbelow': True,
        'axes.grid': True,
        'grid.linewidth': 0.5,
        'grid.linestyle': '-',
        'grid.alpha': .6,
        'lines.linewidth': 1,
        'lines.markersize': 4,
        'lines.markeredgewidth': 1,
        'pgf.preamble': [
            r'\usepackage[utf8x]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            rf'\usepackage{{{typeface}}}'
        ]
    }
    mpl.rcParams.update(pgf_with_latex)
    return pgf_with_latex


def newfig(width_scale,
           height_scale=None,
           aspect=None,
           text_width=390,
           multiple_axes=False):
    """creates a new figure"""
    mpl.use('pgf')
    import matplotlib.pyplot as plt

    if multiple_axes is False:
        fig = plt.figure(figsize=figure_size(
            width_scale,
            height_scale=height_scale,
            aspect=aspect,
            text_width=text_width))
        ax = fig.add_subplot(111)
        return fig, ax

    elif multiple_axes is True:
        fig = plt.figure(figsize=figure_size(
            width_scale,
            height_scale=height_scale,
            aspect=aspect,
            text_width=text_width))
        return fig
