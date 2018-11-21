import flask

app = flask.Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return flask.render_template('index.html')
