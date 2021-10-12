import pytest
from django.contrib.auth.models import User
from TransportApp.models import Orders, Transport, Cars, Drivers


@pytest.fixture
def cars():
    lst = []
    for car in range(10):
        lst.append(Cars.objects.create(name='car'))
    return lst
