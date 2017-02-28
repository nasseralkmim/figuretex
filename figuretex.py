import numpy as np
import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt


def figsize(scale, aspect=None, page_width=390):
    fig_width_pt = page_width
    # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27
    # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0
    # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale
    # width in inches
    fig_height = fig_width*golden_mean
    # height in inches
    if aspect == 'equal':
        fig_size = [fig_width, fig_width]
    else:
        fig_size = [fig_width, fig_height]
    return fig_size


pgf_with_latex = {
    # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",
    # change this if using xetex or lautex
    "text.usetex": True,
    # use LaTeX to write all text
    "font.family": "serif",
    "font.serif": [],
    # blank entries should cause plots to inherit fonts from the document
    "font.sans-serif": [],
    "font.monospace": [],
    "axes.labelsize": 10,
    # LaTeX default is 10pt font.
    "font.size": 8,
    "legend.fontsize": 6,
    # Make the legend/label fonts a little smaller
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.figsize": figsize(.9),
    # default fig size of 0.9 textwidth
    "axes.grid": False,
    "lines.linewidth": 1,
    "lines.markersize": 3,
    "pgf.preamble": [
        r"\usepackage[utf8x]{inputenc}",
        # use utf8 fonts becasue your computer can handle it :)
        r"\usepackage[T1]{fontenc}",
        # plots will be generated using this preamble
        ]
    }
mpl.rcParams.update(pgf_with_latex)


def newfig(width, aspect=None):
    # plt.clf()
    # plt.style.use('seaborn-paper')
    fig = plt.figure(figsize=figsize(width, aspect))
    ax = fig.add_subplot(111)
    return fig, ax


def savefig(filename):
    plt.savefig('{}.pgf'.format(filename), bbox_inches='tight')
    plt.savefig('{}.pdf'.format(filename), bbox_inches='tight')
