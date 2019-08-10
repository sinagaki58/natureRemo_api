from entrypoint import *
from util import parse_date_time
from repository import fetch, post
from flask import Flask, jsonify, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('get_temperature'))


@app.route('/temperature')
def get_temperature():
    res = fetch(DEVICES)
    temperatures = res.json()[0]['newest_events']['te']
    temperature = {
        'time': parse_date_time(temperatures['created_at']),
        'value': temperatures['val']
    }
    return make_response(jsonify(temperature))


@app.route('/users')
def get_users():
    res = fetch(USERS)
    return make_response(jsonify(res.json()))


@app.route('/devices')
def get_devices():
    res = fetch(DEVICES)
    return make_response(jsonify(res.json()))


@app.route('/appliances')
def get_apploances():
    res = fetch(APPLIANCES)
    return make_response(jsonify(res.json()))


AIRCON_ID = '9d348ad6-7269-4f4a-a0e7-e56e1c6c9a23'
@app.route('/signals')
def get_aircon_signals():
    res = fetch(APPLIANCES + '/' + AIRCON_ID + SIGNALS)
    return make_response(jsonify(res.json()))


if __name__ == '__main__':
    app.run(debug=True)
