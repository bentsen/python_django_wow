import os
import time
from dotenv import load_dotenv
import requests
from .models import BlizzardToken

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
token = None
token_expiry = 2000000000000
token_lock = object


def get_data_from_api(region, path, params):
    params['access_token'] = create_access_token()
    url = 'https://%s.api.blizzard.com%s' % (region, path)
    response = requests.get(url, params)
    data = response.json()
    return data


def create_access_token(region='eu'):
    if is_token_valid():
        global token_expiry
        global token

        data = {'grant_type': 'client_credentials'}
        response = requests.post('https://%s.battle.net/oauth/token' % region, data=data,
                                 auth=(client_id, client_secret)).json()

        token_response = BlizzardToken(access_token=response.get('access_token'),
                                       token_type=response.get('token_type'), expires_in=response.get('expires_in'))

        token_expiry = token_response.expires_in
        token = token_response.access_token

    return token


def is_token_valid():
    if token_lock or token_lock is None:
        return True
    return token_expiry > time.time()
