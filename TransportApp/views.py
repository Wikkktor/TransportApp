from django.shortcuts import render
import folium
from TransportApp import forms
from TransportApp.models import Cars, Transport, Orders, Drivers
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView


class IndexView(View):
    def get(self, request):
        my_map = folium.Map(location=[52.100052000000005, 20.804530483807866], zoom_start=16)
        test = folium.Html('<b>Hello world</b>', script=True)
        popup = folium.Popup(test, max_width=2650)
        folium.RegularPolygonMarker(location=[52.100052000000005, 20.804530483807866], popup=popup).add_to(my_map)
        my_map = my_map._repr_html_()
        context = {'my_map': my_map}
        response = render(request, 'base.html', context)
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


class OrderDetailView(DeleteView):
    model = Orders
    template_name = "detail_order.html"
