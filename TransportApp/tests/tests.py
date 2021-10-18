import pytest
from django.test import TestCase, Client
from django.urls import reverse

from TransportApp.models import Cars, Drivers


@pytest.mark.django_db
def test_index_view_not_logged():
    client = Client()
    response = client.get(reverse('base'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_index_view_logged(login):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('base'))
    assert response.status_code == 200


def test_empty_post_index_view_not_logged():
    client = Client()
    response = client.post(reverse("base"))
    assert response.status_code == 302


@pytest.mark.django_db
def test_empty_post_index_view_logged(login):
    client = Client()
    client.force_login(login)
    response = client.post(reverse("base"))
    assert response.status_code == 405


@pytest.mark.django_db
def test_car_list_is_not_empty(login, cars):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('car_list_view'))
    assert response.status_code == 200
    cars_list = response.context['object_list']
    assert cars_list.count() == len(cars)
    for car in cars:
        assert car in cars_list


@pytest.mark.django_db
def test_driver_list_is_not_empty(login, drivers):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('driver_list_view'))
    assert response.status_code == 200
    drivers_list = response.context['object_list']
    assert drivers_list.count() == len(drivers)
    for driver in drivers:
        assert driver in drivers_list


@pytest.mark.django_db
def test_order_list_is_not_empty(login, orders):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('order_list_view'))
    assert response.status_code == 200
    orders_list = response.context['object_list']
    assert orders_list.count() == len(orders)
    for order in orders:
        assert order in orders_list


@pytest.mark.django_db
def test_transport_list_is_not_empty(login, transports):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('transport_list_view'))
    assert response.status_code == 200
    transports_list = response.context['object_list']
    assert transports_list.count() == len(transports)
    for transport in transports:
        assert transport in transports_list


def test_car_add_get_not_logged():
    client = Client()
    response = client.get(reverse('car_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_car_add_get_logged(login):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('car_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_car_add_post(login):
    client = Client()
    client.force_login(login)
    a = {
        'name': 'HDS'
    }
    response = client.post(reverse('car_add_view'), data=a)
    assert response.status_code == 302
    Cars.objects.get(**a)


def test_driver_add_get_not_logged():
    client = Client()
    response = client.get(reverse('driver_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_driver_add_get_logged(login):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('driver_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_driver_add_post(login):
    client = Client()
    client.force_login(login)
    a = {
        'name': 'Albert'
    }
    response = client.post(reverse('driver_add_view'), data=a)
    assert response.status_code == 302
    Drivers.objects.get(**a)


def test_order_add_get_not_logged():
    client = Client()
    response = client.get(reverse('order_add_view'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_order_add_get_logged(login):
    client = Client()
    client.force_login(login)
    response = client.get(reverse('order_add_view'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_add_post(login):
    client = Client()
    client.force_login(login)
    a = {
        'client': 'Albert',
        'phone_number': 333222111,
        'delivery_address': 'Narcyzowa 8 Kanie',
        'delivery_day': '2021-10-28',
        'delivery_hour': '16:00:00',
        'status': 1,
        'opis': 'Test',
    }
    response = client.post(reverse('order_add_view'), data=a)
    assert response.status_code == 302
    # Drivers.objects.get(**a)

