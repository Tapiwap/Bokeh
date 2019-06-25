from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.plotting import figure

scatter_ = figure(plot_width = 400, plot_height = 400, title="My Scatter Plot")

x_axis_ = [1, 2, 3, 4, 5]
y_axis_ = [6, 7, 2, 4, 6]
scatter_.circle(x_axis_,y_axis_, size = 20, alpha = 0.6)
#show(scatter_)

layout = column(scatter_)

curdoc().add_root(layout)
