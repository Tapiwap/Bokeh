from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from random import randrange
import requests
from bs4 import BeautifulSoup

# create the figure
fig = figure()

# Create the web scrapping function
def extract_value():
    r = requests.get("http://bitcoincharts.com/markets/bitstampUSD.html",headers={'User-Agent':'Mozilla/5.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    value_raw = soup.find_all("p")
    value_net = float(value_raw[0].span.text)
    return value_net

# create columndatasource
source = ColumnDataSource(dict(x=[1], y=[extract_value()]))

# create glyphs
fig.circle(x = 'x', y = 'y', color = 'red', line_color = 'blue', source = source)
fig.line(x = 'x', y = 'y', source = source)

def update():
    new_data=dict(x=[source.data['x'][-1]+1],y=[extract_value()])
    source.stream(new_data,rollover=25)
    print(source.data)

# add figure to curdoc and configure callback
curdoc().add_root(fig)
curdoc().add_periodic_callback(update, 6000)