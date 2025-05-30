import json

import pytest
import requests
from docutils.parsers import null
from docutils.parsers.rst.directives import body
from faker import Faker
from pytest_steps import test_steps

from modules.list_methods import create_list, update_list

fake=Faker()

my_headers = {'Authorization': 'pk_188620723_ENHZK1NU6SCPB9FZSEWKF0P5DUK7PND0'}

@pytest.fixture()
def read_file():
    with open('test-data/lists.json', 'r') as file:
        data = json.load(file)
        return data

# def print_name():
#     print('hello')
#     print('bye')
#
def test_checkfixture(read_file):
   list_response = read_file['lists']
   print(list_response)

def test_get_list():
    result= requests.get('https://api.clickup.com/api/v2/folder/90157113236/list', headers = my_headers )
    assert result.status_code == 200
    print('test 1 passed')
    # assert result.json()['lists'][0]['name'] == '1212121'
    # print('test 2 passed')

def test_create_list():
    result = create_list()
    random_name = result.json()['name']
    assert result.status_code == 200
    assert result.json()['name'] == random_name

@test_steps('Create new list', 'Update created list')
def test_update_list():
    result = create_list()
    list_id=result.json()['id']
    yield
    update_list(list_id)
    assert result.status_code == 200
    yield
    assert result.json()['name'] == random_name_for_update
    yield


@pytest.mark.parametrize('id, status',[
                        (null, 400),
                        ('90157113236',200),
                        ("sdfds",200)
])
def test_get_patameterised_list(id,status):
    result= requests.get('https://api.clickup.com/api/v2/folder/'+ id +'/list', headers = my_headers )
