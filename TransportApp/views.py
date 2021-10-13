from django.shortcuts import render
import folium
from TransportApp import forms
from TransportApp.models import Cars, Transport, Orders, Drivers
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, DetailView


class IndexView(View):
    def get(self, request):
        orders = Orders.objects.all().filter(status=1)
        my_map = folium.Map(location=[52.100052000000005, 20.804530483807866], zoom_start=16)
        folium.Marker(location=[52.100052000000005, 20.804530483807866], popup="Kabex").add_to(my_map)
        my_map = my_map._repr_html_()
        context = {'my_map': my_map, 'orders': orders}
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


class OrderDetailView(DetailView):
    model = Orders
    template_name = "detail_order.html"

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        location_order = Orders.objects.get()
        detail_map = folium.Map(location=[52.100052000000005, 20.804530483807866], zoom_start=16)
        folium.Marker(
            location=[52.12407735, 20.796900403084333],
            popup="Wiktor Karaszewicz",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(detail_map)
        context['my_map'] = detail_map._repr_html_()
        return context
