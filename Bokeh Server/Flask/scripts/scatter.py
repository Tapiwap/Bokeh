import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

def create_figure(name = 'Rue'):
    """
    This is for Rue

    """
    fig = figure(plot_width = 400, plot_height = 400, title="My Scatter Plot")
    x_axis_ = [1, 2, 3, 4, 5]
    y_axis_ = [6, 7, 2, 4, 6]
    fig.circle(x_axis_, y_axis_, size = 20, alpha = 0.6)
    return fig