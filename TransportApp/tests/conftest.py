import pytest
from django.contrib.auth.models import User
from TransportApp.models import Orders, Transport, Cars, Drivers


@pytest.fixture
def cars():
    lst = []
    for car in range(10):
        lst.append(Cars.objects.create(name='car'))
    return lst


@pytest.fixture
def drivers():
    lst = []
    for driver in range(10):
        lst.append(Drivers.objects.create(name='driver'))
    return lst


@pytest.fixture
def orders():
    lst = []
    for order in range(10):
        lst.append(Orders.objects.create(
            client="John", phone_number=1231, delivery_address="Warsaw",
            delivery_time='2012-09-04 06:00:00.000000-08:00'))
    return lst


# @pytest.fixture
# def transports(orders, drivers, cars):
#     lst = []
#     for x in range(10):
#         lst.append(Transport.objects.create(
#             car=cars[x], driver=drivers[x], order=orders[x]
#         ))
#     return lst
