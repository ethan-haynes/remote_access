import json
from flask import Flask
from getdiskusage import getdiskusage

app = Flask(__name__)

@app.route("/")
def index():
    return { "/diskusage/<string:path>": "A route that provides disk usage given a file path in the URL" }

@app.route("/diskusage/<path:subpath>")
def getdiskusage_route(subpath):
    return getdiskusage(subpath)
