#!/usr/bin/python3
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.teardown_appcontext
def teardown(error):
    """ close after request """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    message = {"error": "Not found"}
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(host=(environ['HBNB_API_HOST']), port=(environ['HBNB_API_PORT']), threaded=True)
