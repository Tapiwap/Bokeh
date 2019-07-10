from flask import Flask, render_template
from bokeh.embed import server_session
from bokeh.client import pull_session

app_url = "http://localhost:5006/main"

app = Flask(__name__)

@app.route("/")
def get_random_generator():

    with pull_session(url=app_url) as session:

        session.document.roots[0].title.text = "Random Generator"

        first_script = server_session(session_id=session.id, url=app_url)

        return render_template("index.html", first_script = first_script, template = "Flask")

if __name__ == '__main__':
    app.run(port=5000, debug=True)