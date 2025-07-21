import pytest
from faker import Faker
from methods.user import UserMethods
from helpers import create_random_user_data

fake = Faker()
user = UserMethods()


@pytest.fixture
def create_and_delete_user():
    payload = create_random_user_data()
    created_response = user.create_user(payload)
    if created_response.status_code == 200:
        access_token = created_response.json().get('accessToken')
        yield {
            'response': created_response,
            'payload': payload,
            'access_token': access_token
        }
        user.delete_user(access_token)
    else:
        yield {
            'response': created_response,
            'payload': payload
        }
