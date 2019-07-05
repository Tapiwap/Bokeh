#import libraries
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import randrange

# create figure
fig = figure(x_range = (0,11), y_range = (0,11))

#create columndatasource
source = ColumnDataSource(data = dict(x = [], y = []))

# create the glyphs
fig.circle(x='x', y='y', size=8, fill_color = 'red', line_color = 'blue', source = source)

# create a periodic function
def update():
    new_data = dict(x=[randrange(1,10)],y=[randrange(1,10)])
    source.stream(new_data, rollover=15)
    print(source.data)

# add figure to curdoc and configure callback
curdoc().add_root(fig)
curdoc().add_periodic_callback(update,1000)