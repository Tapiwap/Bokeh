#importing libraries
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RadioButtonGroup
from bokeh.layouts import layout

# create column data source
source = ColumnDataSource(dict(average_grades=["B+","A","D-"],
                             exam_grades=["A+","C","D"],
                             student_names=["Stephan","Helder","Riazudidn"]))

#create the figure
f = figure(x_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"],
           y_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"])

#add labels for glyphs
labels=LabelSet(x="average_grades",y="exam_grades",text="student_names",x_offset=5, y_offset=5, source=source)
f.add_layout(labels)

#create glyphs
f.circle(x="average_grades", y="exam_grades", source=source, size=8)

def update_labels(attr,old,new):
    labels.text = options[radio_button_group.active]

#create radio buttons widget
options=["average_grades","exam_grades","student_names"]
radio_button_group=RadioButtonGroup(labels=options)
radio_button_group.on_change("active",update_labels)

#create layout and add to curdoc
lay_out=layout([[radio_button_group]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
