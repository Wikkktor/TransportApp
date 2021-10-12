from django.core.checks import messages
from django.shortcuts import render
import folium
from TransportApp import forms
from TransportApp.models import Cars, Transport, Orders, Drivers
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView


class IndexView(View):
    def get(self, request):
        orders = Orders.objects.all()
        response = render(request, 'base.html', {'orders': orders})
        return response


class CarAddView(CreateView):
    model = Cars
    template_name = 'form.html'
    form_class = forms.CarsModelForm


class CarListView(ListView):
    model = Cars
    template_name = 'cars.html'


class CarDeleteView(DeleteView):
    model = Cars
    template_name = 'form.html'
    success_url = '/'


class DriverAddView(CreateView):
    model = Drivers
    template_name = 'form.html'
    form_class = forms.DriversModelForm


class DriverListView(ListView):
    model = Drivers
    template_name = 'drivers.html'


class DriverDeleteView(DeleteView):
    model = Drivers
    template_name = 'form.html'
    success_url = '/'


class TransportAddView(CreateView):
    model = Transport
    template_name = 'form.html'
    form_class = forms.TransportModelForm


class TransportListView(ListView):
    model = Transport
    template_name = 'transports.html'


class TransportDeleteView(DeleteView):
    model = Transport
    template_name = 'form.html'
    success_url = '/'


class OrderAddView(CreateView):
    model = Orders
    template_name = 'form.html'
    form_class = forms.OrdersModelForm


class OrderListView(ListView):
    model = Orders
    template_name = 'orders.html'


class OrderDeleteView(DeleteView):
    model = Orders
    template_name = 'form.html'
    success_url = '/'
