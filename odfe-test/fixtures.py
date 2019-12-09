from pytest import fixture
import requests
import string
from test_data import *
import json
import random

es_url = 'https://localhost:9200/'
index_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
print(index_name)

@fixture()
def get_request():
    r = create_get_request_obj(node_url=es_url)
    return r


@fixture()
def get_cat_nodes():
    node_url = es_url + '_cat/nodes?v'
    r = create_get_request_obj(node_url=node_url)
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


def create_get_request_obj(node_url, params=None, headers=None):
    req = requests.get(url=node_url, auth = ('admin', 'admin'), verify = False, timeout = 3, params=params, headers=headers)
    return req