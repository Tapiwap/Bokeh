from bokeh.models.widgets import Div
from bokeh.io import curdoc

i = 6
def add_numbers():
    i += 1
    return 34 + i

number = add_numbers()
div = Div(
    text = str(number),
    width=20, 
    height=10
)

curdoc().add_periodic_callback(add_numbers, 2000)
curdoc().add_root(div)