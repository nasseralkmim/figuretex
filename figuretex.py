import numpy as np
import matplotlib as mpl
import itertools
mpl.use('pgf')


MARKER = itertools.cycle(('o', 's', '^', '*', '>', '<', '8', 'p'))
LINES = itertools.cycle(("--", ":", "-.", "-"))


def figure_size(width_scale, height_scale=None, aspect=None, text_width=390):
    fig_width_pt = text_width
    # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27
    # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0
    # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*width_scale

    if height_scale is None:
        # width_scale in inches
        fig_height = fig_width*golden_mean
    else:
        fig_height = fig_width*height_scale

    if aspect == 'equal':
        fig_size = [fig_width, fig_width]
    else:
        fig_size = [fig_width, fig_height]

    return fig_size


pgf_with_latex = {
    # LaTeX default is 10pt font.
    "text.usetex": True,
    # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",
    # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],
    # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "font.size": 8,
    "figure.titlesize": 8,

    "legend.fontsize": 8,
    "legend.markerscale": .9,
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

    # Make the legend/label fonts a little smaller
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    # 'xtick.major.size': 6,
    # 'xtick.major.size': 6,
    # 'xtick.minor.size' : 2,
    # 'xtick.minor.size' : 2,

    "axes.titlesize": 8,
    'axes.spines.left': True,
    'axes.spines.top': True,
    'axes.spines.bottom': True,
    'axes.spines.right': True,
    'axes.labelsize': 9,
    'axes.linewidth': 1,
    # 'axes.xmargin':0,
    # 'axes.ymargin':0, #no good, it cuts data out

    'axes.axisbelow': True,
    'axes.grid': True,
    'grid.linewidth': 0.5,
    'grid.linestyle': '-',
    'grid.alpha': .6,
    'lines.linewidth': 1,
    'lines.markersize': 4,
    'lines.markeredgewidth': 1,

    'pgf.preamble': [
        r'\usepackage[utf8]{inputenc}',
        r'\usepackage{microtype}'
        # use utf8 fonts becasue your computer can handle it :)
        r'\usepackage[T1]{fontenc}',
        # plots will be generated using this preamble
        ]
    }
mpl.rcParams.update(pgf_with_latex)


def newfig(width_scale, height_scale=None, aspect=None,
           text_width=390, multiple_axes=False):
    import matplotlib.pyplot as plt

    if multiple_axes is False:
        fig = plt.figure(figsize=figure_size(width_scale,
                                             height_scale=height_scale,
                                             aspect=aspect,
                                             text_width=text_width))
        ax = fig.add_subplot(111)
        return fig, ax

    elif multiple_axes is True:
        fig = plt.figure(figsize=figure_size(width_scale,
                                             height_scale=height_scale,
                                             aspect=aspect,
                                             text_width=text_width))
        return fig


def savefig(filename, fig=None):
    import matplotlib.pyplot as plt
    if fig is None:
        plt.savefig('{}.pgf'.format(filename), bbox_inches='tight')
        plt.savefig('{}.pdf'.format(filename), bbox_inches='tight')
    else:
        fig.savefig('{}.pgf'.format(filename), bbox_inches='tight')
        fig.savefig('{}.pdf'.format(filename), bbox_inches='tight')
    plt.close('all')


def show(filename):
    import os
    os.system('start {}.pdf'.format(filename))
