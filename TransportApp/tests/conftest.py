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
            delivery_day='2012-09-04', delivery_hour= '16:30:00'))
    return lst


@pytest.fixture
def transports(orders, drivers, cars):
    lst = []
    for x in range(10):
        car = cars[x]
        driver = drivers[x]
        t = Transport.objects.create(car=car, driver=driver)
        order = orders[x]
        t.order.add(order)
        lst.append(t)
    return lst


@pytest.fixture
def login():
    return User.objects.create(username='Adam')