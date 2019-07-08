# Hello Flask app
from flask import Flask, render_template, request
from scatter import create_figure
from bokeh.embed import components

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get('name')
    if name == None:
        name = 'Tapiwa'

    plot = create_figure()

    script, div = components(plot)

    return render_template('index.html', script=script, div = div, 
                            name = name)

if __name__ == '__main__':
    app.run(port=5000, debug=True)