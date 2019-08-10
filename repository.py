import os
import requests

BASE_URL = 'https://api.nature.global/1'


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
