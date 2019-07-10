from bokeh.io import curdoc

from scatter import create_scatter_plot
from random_generator import create_random_gen_plot, update

scatter_plot = create_scatter_plot()
random_gen_plot = create_random_gen_plot()

curdoc().add_root(scatter_plot)
curdoc().add_root(random_gen_plot)
curdoc().add_periodic_callback(update, 1000)
