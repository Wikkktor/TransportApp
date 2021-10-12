import pytest
from django.test import TestCase, Client
from django.urls import reverse
from conftest import cars

def test_index_view():
    client = Client()
    response = client.get(reverse('base'))
    assert response.status_code == 200


def test_empty_post_index_view():
    client = Client()
    response = client.post(reverse("base"))
    assert response.status_code == 405


@pytest.mark.django_db
def test_car_list_is_not_empty(cars):
    client = Client()
    response = client.get(reverse('car_list_view'))
    assert response.status_code == 200
    cars_list = response.context['object_list']
    assert cars_list.count() == len(cars)
    for car in cars:
        assert car in cars_list
