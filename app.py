import flask
from flask import request
from main import getmsg

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    tittle = request.args.get('tittle')
    return getmsg(tittle)

app.run()
