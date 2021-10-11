from django.core.checks import messages
from django.shortcuts import render

from TransportApp import forms
from TransportApp.models import Cars, Transport, Orders, Drivers
from django.views import View
from django.views.generic import CreateView


class IndexView(View):
    def get(self, request):
        response = render(request, 'base.html')
        return response


class CarAddView(CreateView):
    model = Cars
    template_name = 'form.html'
    form_class = forms.CarsModelForm
    success_url = "/"


class DriverAddView(CreateView):
    model = Drivers
    template_name = 'form.html'
    form_class = forms.DriversModelForm
    success_url = "/"


class TransportAddView(CreateView):
    model = Transport
    template_name = 'form.html'
    form_class = forms.TransportModelForm
    success_url = "/"


class OrderAddView(CreateView):
    model = Orders
    template_name = 'form.html'
    form_class = forms.OrdersModelForm
    success_url = "/"
