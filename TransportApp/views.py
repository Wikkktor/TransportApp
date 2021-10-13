from django.shortcuts import render
import folium
from TransportApp.geocode import get_location_geo
from TransportApp import forms
from TransportApp.models import Cars, Transport, Orders, Drivers
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView


class IndexView(View):
    # Main base view: list of unrealized orders with markers on map
    def get(self, request):
        orders = Orders.objects.all().filter(status=1)
        my_map = folium.Map(location=[52.100052000000005, 20.804530483807866], zoom_start=16)
        folium.Marker(location=[52.100052000000005, 20.804530483807866],
                      popup="Kabex", icon=folium.Icon(color="blue")).add_to(my_map)
        for order in orders:
            location = get_location_geo(order.delivery_address)
            name = order.client
            folium.Marker(
                location=location,
                popup=name,
                icon=folium.Icon("red")
            ).add_to(my_map)
        context = {'my_map': my_map._repr_html_(), 'orders': orders}
        response = render(request, 'base.html', context)
        return response


class CarAddView(CreateView):
    # Adding by form view
    model = Cars
    template_name = 'form.html'
    form_class = forms.CarsModelForm


class CarListView(ListView):
    # List View
    model = Cars
    template_name = 'cars.html'


class CarDeleteView(DeleteView):
    # Deleting view
    model = Cars
    template_name = 'form.html'
    success_url = '/'


class DriverAddView(CreateView):
    # Adding by form view
    model = Drivers
    template_name = 'form.html'
    form_class = forms.DriversModelForm


class DriverListView(ListView):
    # List view
    model = Drivers
    template_name = 'drivers.html'


class DriverDeleteView(DeleteView):
    # Deleting View
    model = Drivers
    template_name = 'form.html'
    success_url = '/'


class TransportAddView(CreateView):
    # Adding by form view
    model = Transport
    template_name = 'form.html'
    form_class = forms.TransportModelForm


class TransportListView(ListView):
    # list view
    model = Transport
    template_name = 'transports.html'


class TransportDeleteView(DeleteView):
    # Deleting view
    model = Transport
    template_name = 'form.html'
    success_url = '/'


class OrderAddView(CreateView):
    # Adding by form view
    model = Orders
    template_name = 'form.html'
    form_class = forms.OrdersModelForm


class OrderListView(ListView):
    # List view
    model = Orders
    template_name = 'orders.html'


class OrderDeleteView(DeleteView):
    # Deleting View
    model = Orders
    template_name = 'delete_order.html'
    success_url = '/'


class DetailOrderView(View):
    # Detail order view with marker with order delivery address on map
    def get(self, request, pk):
        order = Orders.objects.get(id=pk)
        adress = order.delivery_address
        geo = get_location_geo(adress)
        detail_map = folium.Map(location=[52.100052000000005, 20.804530483807866], zoom_start=16)
        folium.Marker(
            location=geo,
            popup=order.client,
            icon=folium.Icon(color='red')
        ).add_to(detail_map)
        folium.Marker(
            location=[52.100052000000005, 20.804530483807866],
            popup="Kabex",
            icon=folium.Icon(color='blue')
        ).add_to(detail_map)
        return render(
            request,
            'detail_order.html',
            {'orders': order, 'my_map': detail_map._repr_html_()}
        )
