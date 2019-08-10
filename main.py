import requests
import os
from entrypoint import *
from flask import Flask, jsonify, make_response, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)


# fetcher
def get_headers():
    token = os.environ['NATURE_REMO']
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    return headers


def fetch(end_point: str):
    url = BASE_URL + end_point
    headers = get_headers()

    try:
        res = requests.get(url, headers=headers)
        return res
    except Exception as e:
        print(e)
        return None


def post(end_point: str):
    url = BASE_URL + end_point
    headers = get_headers()

    try:
        res = requests.post(url, headers=headers)
        return res
    except Exception as e:
        print(e)
        return None


# util
def parse_date_time(date_str: str):
    tz_jst = timedelta(hours=9)
    date_str = date_str.replace('Z', '')
    return (datetime.fromisoformat(date_str) + tz_jst).strftime('%Y-%m-%d %H:%M:%S')
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
