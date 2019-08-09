import requests
import os
from entrypoint import *
from flask import Flask, jsonify, make_response

app = Flask(__name__)


def fetch(end_point: str):
    token = os.environ['NATURE_REMO']
    base_url = 'https://api.nature.global/1'
    url = base_url + end_point
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    try:
        res = requests.get(url, headers=headers)
        return res
    except Exception as e:
        print(e)
        return None


@app.route('/temperature')
def get_temperature():
    res = fetch(DEVICES)
    temperature = res.json()[0]['newest_events']['te']
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


if __name__ == '__main__':
    app.run()
