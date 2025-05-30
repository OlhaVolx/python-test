import requests
from faker import Faker
fake=Faker()

my_headers = {'Authorization': 'pk_188620723_ENHZK1NU6SCPB9FZSEWKF0P5DUK7PND0'}
def create_list():
    random_name = fake.first_name()

    body = {
        "name": random_name
    }
    return requests.post('https://api.clickup.com/api/v2/folder/90157113236/list', headers=my_headers, json=body)

def update_list(list_id):
    random_name_for_update = fake.first_name()
    body_updated = {
        "name": random_name_for_update
    }
    result = requests.put('https://api.clickup.com/api/v2/list/' + list_id, headers=my_headers, json=body_updated)