from django.db import models
from django.urls import reverse


class Orders(models.Model):
    DELIVERY_STATUS = [
        (1, "Nowe"),
        (2, "W realizacji"),
        (3, "Zrealizowane")
    ]
    client = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    delivery_address = models.CharField(max_length=300)
    delivery_time = models.DateTimeField()
    status = models.IntegerField(choices=DELIVERY_STATUS, default=1)
    opis = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('order_list_view')

    def __str__(self):
        return "Dane " + self.client + " Adres " + self.delivery_address


class Drivers(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('driver_list_view')

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('car_list_view')

    def __str__(self):
        return self.name


class Transport(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    order = models.ManyToManyField(Orders)

    def get_absolute_url(self):
        return reverse('transport_list_view')

    def __str__(self):
        name = f"Samochód: {self.car.name} Kierowca: {self.driver.name} zamówienie: {self.order.name}"
        return name
