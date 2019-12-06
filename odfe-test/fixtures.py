from pytest import fixture
import requests
from requests import Timeout, ConnectionError, ConnectTimeout
import random, string
from test_data import *
import json

es_url = 'https://localhost:9200/'
index_name = ''.join(random.choices(string.ascii_lowercase, k=7))
print(index_name)

@fixture()
def get_request():
    try:
        r = requests.get(url=es_url, auth = ('admin', 'admin'), verify = False, timeout = 3)
    except ConnectTimeout as e:
        return e
    return r


@fixture()
def get_cat_nodes():
    node_url = es_url + '_cat/nodes?v'
    r = requests.get(url=node_url, auth = ('admin', 'admin'), verify = False, timeout = 3)
    return r


@fixture()
def create_index():
    node_url = es_url + index_name
    r = requests.put(url=node_url, auth = ('admin', 'admin'), verify = False, timeout = 3)
    return r


@fixture()
def create_index_mapping():
    node_url = es_url + index_name + '/' + '_mappings'
    r =requests.put(url=node_url, auth = ('admin', 'admin'), verify = False, headers=req_headers, data=json.dumps(index_payload))
    return r


@fixture()
def load_test_data():
    node_url = es_url + index_name + '/' + '_doc/'
    r = requests.post(url=node_url, params=params, auth = ('admin', 'admin'), verify = False, headers=req_headers, data=json.dumps(test_data))
    return r