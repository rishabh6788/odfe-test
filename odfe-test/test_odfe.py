from fixtures import *


def test_es_run(get_request):
    assert get_request.status_code == 200


def test_cat_nodes(get_cat_nodes):
    assert get_cat_nodes.status_code == 200


def test_create_index(create_index):
    assert create_index.status_code == 200


def test_create_mapping(create_index_mapping):
    assert create_index_mapping.json() == {'acknowledged': True}


def test_load_data(load_test_data):
    assert load_test_data.status_code == 201
