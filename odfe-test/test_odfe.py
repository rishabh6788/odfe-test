from fixtures import *
import pytest
import math


def test_es_run(get_request):
    assert get_request.status_code == 200

def test_cat_nodes(get_cat_nodes):
    assert get_cat_nodes.status_code == 200



