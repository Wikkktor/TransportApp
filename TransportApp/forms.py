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


class TransportUpdateForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('car', 'driver')
        labels = {
            'car': 'Samochód',
            'driver': 'Kierowca',
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


class OrdersModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrdersModelForm, self).__init__(*args, **kwargs)
        self.fields['opis'].required = False

    class Meta:
        model = Orders
        fields = ('client', 'phone_number', 'delivery_address', 'delivery_day', 'delivery_hour', 'opis')
        widgets = {
            'delivery_day': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'delivery_hour': forms.TimeInput(attrs={'type': 'time', 'value': '15:00', 'class': 'form-control'}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Client name'}),
            'opis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional information'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '555444333'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Delivery address'}),
        }


class TransportForm(forms.Form):
    car = forms.ModelChoiceField(queryset=Cars.objects.all(), label="Samochód")
    driver = forms.ModelChoiceField(queryset=Drivers.objects.all(), label='Kierowca')
