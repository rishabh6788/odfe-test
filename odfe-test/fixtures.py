from pytest import fixture
import requests

es_url = 'https://localhost:9200/'


@fixture()
def get_request():
    try:
        r = requests.get(url=es_url, auth = ('admin', 'admin'), verify = False, timeout = 3)
    except TimeoutError as e:
        return r
    return r


@fixture()
def get_cat_nodes():
    node_url = es_url + '_cat/nodes?v'
    r = requests.get(url=node_url, auth = ('admin', 'admin'), verify = False, timeout = 3)
    return r
