from datetime import date, datetime

from django.db import models
from django.urls import reverse


class Orders(models.Model):
    DELIVERY_STATUS = [
        (1, "Nowe"),
        (2, "Zdefiniowano Transport"),
        (3, "Zrealizowane"),
        (4, 'Anulowane')
    ]
    client = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    delivery_address = models.CharField(max_length=300)
    delivery_day = models.DateField(default=date.today)
    delivery_hour = models.TimeField(default=datetime.now)
    status = models.IntegerField(choices=DELIVERY_STATUS, default=1)
    opis = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length=300, null=True)
    lon = models.CharField(max_length=300, null=True)

    def get_absolute_url(self):
        return reverse('order_detail_view', args=(self.pk,))

    def get_delete_url(self):
        return reverse('order_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('order_update_view', args=(self.pk,))

    def __str__(self):
        return self.client + "\n" " Adres " + self.delivery_address + " Data " + str(self.delivery_day)


class Drivers(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('driver_list_view')

    def get_delete_url(self):
        return reverse('driver_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('driver_update_view', args=(self.pk,))

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('car_list_view')

    def get_delete_url(self):
        return reverse('car_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('car_modify_view', args=(self.pk,))

    def __str__(self):
        return self.name


class Transport(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    order = models.ManyToManyField(Orders)

    def get_absolute_url(self):
        return reverse('transport_list_view')

    def get_delete_url(self):
        return reverse('transport_delete_view', args=(self.pk,))

    def get_modify_url(self):
        return reverse('transport_update_view', args=(self.pk,))

    def __str__(self):
        name = f"Samochód: {self.car.name} Kierowca: {self.driver.name} zamówienie: {self.order.name}"
        return name
