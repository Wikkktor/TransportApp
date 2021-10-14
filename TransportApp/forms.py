from django import forms
from TransportApp.models import Cars, Transport, Orders, Drivers


class CarsModelForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'
        labels = {
            'name': 'Nazwa pojazdu'
        }


class DriversModelForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = '__all__'
        labels = {
            'name': 'Nazwa kierowcy'
        }


class TransportModelForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = '__all__'
        labels = {
            'car': 'Samochód',
            'driver': 'Kierowca',
            'order': 'Zamówienie'
        }


class DateInput(forms.DateTimeInput):
    input_type = "datetime-local"


class OrdersModelForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'
        labels = {
            'client': 'Klient',
            'phone_number': 'Numer Telefonu',
            'delivery_address': 'Adres dostawy',
            'delivery_time': 'Termin dostawy',
            'opis': 'Dodatkowe info',
            'status': 'Status zamówienia'
        }
        widgets = {
            'delivery_time': DateInput,
        }
