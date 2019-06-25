from bokeh.io import curdoc, show
from bokeh.plotting import figure
from bokeh.layouts import gridplot
from bokeh.models.widgets import Button


# create some widgets
button = Button(label="Alter Graph")

# Create a list of numbers from 0 to 10
x = list(range(11))

# Set y0 to x
# set y1 to 10 - x (reverse)
# get an array of the absolute numbers of x
y0, y1, y2 = x, [10-i for i in x], [abs(i-5) for i in x]

# create first plot
s1 = figure(width=250, plot_height=250)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create second plot
s2 = figure(width=250, plot_height=250)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create third plot
s3 = figure(width=250, plot_height=250)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

def alter_y1():
    y0 = [10 - 2 for i in x]
    s1 = figure(width=250, plot_height=250)
    s1.circle(x, y0, size=10, color="navy", alpha=0.5)

button.on_click(alter_y1)

grid = [[s1, s2], [s3, button]]

layout = gridplot(grid, toolbar_location=None)

curdoc().add_root(layout)