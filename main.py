import requests
import os

if __name__ == '__main__':
    token = os.environ['NATURE_REMO']
    cloudBaseUrl = 'https://api.nature.global/1'
    endPoint = '/devices'
    cloudUrl = cloudBaseUrl + endPoint
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    try:
        res = requests.get(cloudUrl, headers=headers)
        print(res.json())
    except Exception as e:
        print(e)
