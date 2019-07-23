from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout
from bokeh.models.widgets import CheckboxGroup

labels = ["Tapiwa", "Melly", "MG", "Ricardo", "Ben"]
distances = [20, 32, 30, 45, 35]

source = ColumnDataSource(data = dict(x = labels, y = distances))

check_boxes = CheckboxGroup(
    labels = labels,
    active = [0]
)

bar_chart = figure( x_range = labels, plot_height = 350, title = "Distance Travelled Per Person")

def update_source(attr, old, new):
    people_to_select = [(check_boxes.labels[index], distances[index]) for index in check_boxes.active]
    source.data = dict(
        x = [tuple_[0] for tuple_ in people_to_select],
        y = [tuple_[1] for tuple_ in people_to_select]
    )
    bar_chart.x_range.factors = [tuple_[0] for tuple_ in people_to_select]
    print(source.data)


def create_chart(source):    
    bar_chart.vbar(x = 'x', top = 'y', width = 0.9, source = source)
    bar_chart.xgrid.grid_line_color = None
    return bar_chart

chart = create_chart(source)

check_boxes.on_change("active", update_source)

lay_out = layout([check_boxes, chart])

curdoc().add_root(lay_out)