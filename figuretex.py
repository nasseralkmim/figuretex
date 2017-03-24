import numpy as np
import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt


def figsize(scale, aspect=None, text_width=390):
    fig_width_pt = text_width
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

    # LaTeX default is 10pt font.
    "font.size": 8,
    "figure.titlesize":8,

    "legend.fontsize": 7,
    "legend.markerscale":.9,
    'legend.numpoints': 1,
    'legend.handlelength': 2,
    'legend.scatterpoints': 1,
    'legend.labelspacing': 0.5,
    'legend.facecolor':'eff0f1',
    'legend.edgecolor':'none',
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

    'figure.figsize': figsize(.9),

    # default fig size of 0.9 textwidth
    "axes.titlesize":8,
    'axes.grid': True,
    'axes.spines.left':True,
    'axes.spines.top':False,
    'axes.spines.bottom':True,
    'axes.spines.right':False,
    'axes.labelsize': 9,
    'axes.linewidth': 1,
    # 'axes.xmargin':0,
    # 'axes.ymargin':0, #no good, it cuts data out

    'grid.linewidth':0.5,
    'grid.linestyle':':',
    'lines.linewidth': 1,
    'lines.markersize': 3,

    'pgf.preamble': [
        r'\usepackage[utf8]{inputenc}',
        r'\usepackage{microtype}'
        # use utf8 fonts becasue your computer can handle it :)
        r'\usepackage[T1]{fontenc}',
        # plots will be generated using this preamble
        ]
    }
mpl.rcParams.update(pgf_with_latex)


def newfig(width, aspect=None, text_width=390):
    # plt.clf()
    plt.style.use('seaborn-muted')
    fig = plt.figure(figsize=figsize(width, aspect, text_width))
    ax = fig.add_subplot(111)
    return fig, ax


def savefig(filename, fig=None):
    if fig is None:
        plt.savefig('{}.pgf'.format(filename), bbox_inches='tight')
        plt.savefig('{}.pdf'.format(filename), bbox_inches='tight')
    else:
        fig.savefig('{}.pgf'.format(filename), bbox_inches='tight')
        fig.savefig('{}.pdf'.format(filename), bbox_inches='tight')
    
