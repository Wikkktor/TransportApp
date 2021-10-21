import django_filters
from django import forms
from django_filters import CharFilter, DateFilter

from TransportApp.models import Orders


class OrderFilter(django_filters.FilterSet):
    client = CharFilter(field_name='client', lookup_expr='icontains', label='Nazwa klienta:',
                        # widgets=forms.TextInput(attrs={'placeholder': 'Nazwa klienta'})
                        )
    phone_number = CharFilter(field_name='phone_number', lookup_expr='icontains', label='Numer Telefonu:',
                        # widgets=forms.NumberInput(attrs={'placeholder': 'Numer telefonu'})
                              )
    delivery_day = DateFilter(field_name='delivery_day', lookup_expr='icontains', label='Data dostarczenia',
                              # widgets=forms.DateInput(attrs={'placeholder': 'Data dostarczenia'})
                              )
    delivery_address = CharFilter(field_name='delivery_address', lookup_expr='icontains', label='Adres dostawy')

    class Meta:
        model = Orders
        fields = ('client', 'phone_number', 'delivery_day', 'delivery_address')
