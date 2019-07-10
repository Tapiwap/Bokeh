from bokeh.io import curdoc
from bokeh.plotting import figure

def create_scatter_plot():
    fig = figure(plot_width = 350, plot_height = 350, title = "THe Other scatter")
    x_axis_ = [1, 2, 3, 4, 5]
    y_axis_ = [6, 7, 2, 4, 6]
    fig.circle(x_axis_, y_axis_, size = 20, alpha = 0.6)
    return fig

#curdoc().add_root(fig)
