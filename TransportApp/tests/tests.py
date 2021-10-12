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


@pytest.mark.django_db
def test_driver_list_is_not_empty(drivers):
    client = Client()
    response = client.get(reverse('driver_list_view'))
    assert response.status_code == 200
    drivers_list = response.context['object_list']
    assert drivers_list.count() == len(drivers)
    for driver in drivers:
        assert driver in drivers_list


@pytest.mark.django_db
def test_order_list_is_not_empty(orders):
    client = Client()
    response = client.get(reverse('order_list_view'))
    assert response.status_code == 200
    orders_list = response.context['object_list']
    assert orders_list.count() == len(orders)
    for order in orders:
        assert order in orders_list


# @pytest.mark.django_db
# def test_order_list_is_not_empty(transports):
#     client = Client()
#     response = client.get(reverse('transport_list_view'))
#     assert response.status_code == 200
#     transports_list = response.context['object_list']
#     assert transports_list.count() == len(transports)
#     for transport in transports:
#         assert transport in transports_list
