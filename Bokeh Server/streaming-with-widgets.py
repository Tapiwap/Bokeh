from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter, Select
from bokeh.layouts import layout
from bokeh.plotting import figure
from random import randrange
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from math import radians
from pytz import timezone

# create figure
fig = figure(x_axis_type = 'datetime')

# Create webscrapping function
def extract_value():
    r = requests.get("http://bitcoincharts.com/markets/btcnCNY.html",headers={'User-Agent':'Mozilla/5.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    value_raw = soup.find_all("p")
    value_net = float(value_raw[0].span.text)
    return value_net

# Create a column data source
source = ColumnDataSource(dict(x=[],y=[]))

# Create the glyphs
fig.circle(x='x',y='y',color='red',line_color='brown',source=source)
fig.line(x='x',y='y',source=source)

# create a periodic update function
def update():
    new_data = dict(x = [datetime.now(tz = timezone('Africa/Gaborone'))], y = [extract_value()])
    source.stream(new_data, rollover=25)
    print(datetime.now(timezone('Africa/Gaborone')))

# create an intermediate callback function
def update_intermediate(attr, old, new):
    update()

fig.xaxis.formatter = DatetimeTickFormatter(
    seconds=["%Y-%m-%d-%H-%m-%S"],
    minsec=["%Y-%m-%d-%H-%m-%S"],
    minutes=["%Y-%m-%d-%H-%m-%S"],
    hourmin=["%Y-%m-%d-%H-%m-%S"],
    hours=["%Y-%m-%d-%H-%m-%S"],
    days=["%Y-%m-%d-%H-%m-%S"],
    months=["%Y-%m-%d-%H-%m-%S"],
    years=["%Y-%m-%d-%H-%m-%S"]
)

fig.xaxis.major_label_orientation = radians(90)

# create a select widget
options = [("okcoinCNY","Okcoin CNY"),("btcnCNY","BTCN China")]
select = Select(title = "Market Name", value = "okcoinCNY", options = options)
select.on_change("value", update_intermediate)

# add figure to curdoc and configure callback
lay_out = layout([[fig], [select]])
curdoc().add_root(lay_out)
curdoc().add_periodic_callback(update, 2000)
