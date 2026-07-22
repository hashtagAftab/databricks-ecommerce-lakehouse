# this file shall have the api util functions

import requests
from config import *


# defining authenticate function
def authenticate(username=USERNAME, password=PASSWORD) -> str:
    """
    generates Access Token for the given user
    Args:
        user (str, optional): username. Defaults to 'emilys'.
        password (str, optional): password. Defaults to 'emilyspass'.
    """

    login_url = f'{BASE_URL}/auth/login'
    payloads = {
        'username': username,
        'password': password
    }

    response = requests.post(login_url, json=payloads)
    response.raise_for_status()

    return response.json()['accessToken']


def fetch_data(endpoint: str, headers: dict[str, str], limit: int= 30, skip: int= 0) -> list:
    """
    gets data from dummyjson.com as sent endpoint
    Args:
        endpoint (str): endpoint to fetch data from
        headers (dict[str, str]): headers to send.
        limit (int, optional): limit of data to fetch. Defaults to 30.
        skip (int, optional): skip number of data. Defaults to 0.
    
    endpoint should be in valid_endpoints: list[str] = ['products', 'carts', 'recipes', 'users', 'posts']
    """

    data_url = f'{BASE_URL}/{endpoint}'
    params = {
        'limit': limit,
        'skip': skip
    }

    response = requests.get(data_url, params=params, headers=headers)
    response.raise_for_status()

    return response.json()[endpoint]