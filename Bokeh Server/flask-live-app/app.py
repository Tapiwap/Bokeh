# Hello Flask app
from flask import Flask, render_template
from bokeh.embed import server_session
from bokeh.client import pull_session

app_url = "http://localhost:5006/random-generator"

app = Flask(__name__)

@app.route("/")
def index():
    # pull new session from running bokeh server
    with pull_session(url=app_url) as session:

        # update or customise that session
        session.document.roots[0].title.text = "Random Generator"

        #Generate a script to load the customised session
        script = server_session(session_id=session.id, url=app_url)

        return render_template("index.html", script = script, template = "Flask")
 
if __name__ == '__main__':
    app.run(port=5000, debug=True)