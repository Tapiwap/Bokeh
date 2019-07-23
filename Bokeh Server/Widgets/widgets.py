# Import libraries
from bokeh.io import curdoc
from bokeh.models.widgets import (Button, 
                                    TextInput, Paragraph,
                                    CheckboxGroup)
from bokeh.layouts import layout

# Initialise objects
text_input = TextInput(value = 'Tapiwa')
button = Button(label = 'Press Me')
check_boxes = CheckboxGroup(labels = ['Tapiwa','Pat McGroin','These Nuts'],
                                      active = [0])
output = Paragraph()

# create a method to greet people
def greet():
    for index in check_boxes.active:
        print("Hello, " +  check_boxes.labels[index])

# make the button clickable
button.on_click(greet)

lay_out = layout([[button, check_boxes], [output]])
curdoc().add_root(lay_out)