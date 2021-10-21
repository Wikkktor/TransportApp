from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
import folium

from TransportApp.filters import OrderFilter
from TransportApp.forms import TransportForm, OrdersModelForm
from TransportApp import forms
from TransportApp.geocode import get_location_geo
from TransportApp.models import Cars, Transport, Orders, Drivers
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django_filters.views import FilterView


class IndexView(LoginRequiredMixin, View):
    # Main base view: list of unrealized orders with markers on map
    def get(self, request):
        orders = Orders.objects.all().filter(status=1).order_by('delivery_day', 'delivery_hour')
        my_map = folium.Map(location=[52.100052000000005, 20.804530483807866], zoom_start=16)
        folium.Marker(location=[52.100052000000005, 20.804530483807866],
                      popup="Kabex", icon=folium.Icon(color="blue")).add_to(my_map)
        for order in orders:
            lat = order.lat
            lon = order.lon
            name = order.client
            folium.Marker(
                location=[lat, lon],
                popup=name,
                icon=folium.Icon("red")
            ).add_to(my_map)
        context = {'my_map': my_map._repr_html_(), 'orders': orders}
        response = render(request, 'base.html', context)
        return response


# Car Views


class CarAddView(LoginRequiredMixin, CreateView):
    # Adding by form view
    model = Cars
    template_name = 'form.html'
    form_class = forms.CarsModelForm


class CarListView(LoginRequiredMixin, ListView):
    # List View
    model = Cars
    template_name = 'cars.html'


class CarDeleteView(LoginRequiredMixin, DeleteView):
    # Deleting view
    model = Cars
    template_name = 'form.html'
    success_url = '/'


class CarUpdateView(LoginRequiredMixin, UpdateView):
    # Modify view
    model = Cars
    template_name = 'form.html'
    fields = '__all__'
    success_url = '/'


class CarDetailView(LoginRequiredMixin, DetailView):
    # Detail View
    model = Cars
    template_name = 'detail_car.html'


class DriverAddView(LoginRequiredMixin, CreateView):
    # Adding by form view
    model = Drivers
    template_name = 'form.html'
    form_class = forms.DriversModelForm


class DriverListView(LoginRequiredMixin, ListView):
    # List view
    model = Drivers
    template_name = 'drivers.html'


class DriverDeleteView(LoginRequiredMixin, DeleteView):
    # Deleting View
    model = Drivers
    template_name = 'form.html'
    success_url = '/'


class DriverUpdateView(LoginRequiredMixin, UpdateView):
    # Modify view
    model = Drivers
    template_name = 'form.html'
    fields = '__all__'
    success_url = '/'


class DriverDetailView(LoginRequiredMixin, DetailView):
    # Detail View
    model = Drivers
    template_name = 'detail_driver.html'


class TransportAddView(LoginRequiredMixin, CreateView):
    # Adding by form view
    model = Transport
    template_name = 'form.html'
    form_class = forms.TransportModelForm


class TransportListView(LoginRequiredMixin, ListView):
    # list view
    model = Transport
    template_name = 'transports.html'


class TransportDeleteView(LoginRequiredMixin, DeleteView):
    # Deleting view
    model = Transport
    template_name = 'form.html'
    success_url = '/'


class TransportUpdateView(LoginRequiredMixin, UpdateView):
    # Modify view
    model = Transport
    template_name = 'form.html'
    fields = '__all__'
    success_url = '/'


class TransportDetailView(LoginRequiredMixin, DetailView):
    # Detail View
    model = Transport
    template_name = 'detail_transport.html'


class OrderAddView(LoginRequiredMixin, View):
    # Add view, localization changes to geocode
    def get(self, request):
        form = OrdersModelForm()
        return render(request,
                      'form.html', {'form': form})

    def post(self, request):
        delivery_adres = request.POST['delivery_address']
        geo = get_location_geo(delivery_adres)
        lat = geo[0]
        lon = geo[1]
        Orders.objects.create(client=request.POST['client'],
                              phone_number=request.POST['phone_number'],
                              delivery_address=delivery_adres,
                              delivery_day=request.POST['delivery_day'],
                              delivery_hour=request.POST['delivery_hour'],
                              status=1,
                              opis=request.POST['opis'],
                              lat=lat,
                              lon=lon,
                              )
        return redirect('/order/list')


class OrderListView(LoginRequiredMixin, View):
    def get(self, request):
        not_done_orders = Orders.objects.all().filter(status=1).order_by('delivery_day', 'delivery_hour')
        in_process_orders = Orders.objects.all().filter(status=2).order_by('delivery_day', 'delivery_hour')
        done_orders = Orders.objects.all().filter(status=3).order_by('delivery_day', 'delivery_hour')
        cancel_orders = Orders.objects.all().filter(status=4).order_by('delivery_day', 'delivery_hour')
        context = {'done_orders': done_orders, 'in_process_orders': in_process_orders,
                   'not_done_orders': not_done_orders, 'cancel_orders': cancel_orders}
        return render(request, 'orders_list_view.html', context)


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    # Deleting View
    model = Orders
    template_name = 'delete_order.html'
    success_url = '/'


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    # Modify view
    model = Orders
    template_name = 'modify_order.html'
    fields = '__all__'
    success_url = '/'


class DetailOrderView(LoginRequiredMixin, View):
    # Detail order view with marker with order delivery address on map and transport form
    def get(self, request, pk):
        order = Orders.objects.get(id=pk)
        detail_map = folium.Map(location=[order.lat, order.lon], zoom_start=16)
        folium.Marker(
            location=[order.lat, order.lon],
            popup=order.client,
            icon=folium.Icon(color='red')
        ).add_to(detail_map)
        folium.Marker(
            location=[52.100052000000005, 20.804530483807866],
            popup="Kabex",
            icon=folium.Icon(color='blue')
        ).add_to(detail_map)
        form = TransportForm()
        return render(
            request,
            'detail_order.html',
            {'order': order, 'my_map': detail_map._repr_html_(), 'form': form})

    def post(self, request, pk):
        driver = Drivers.objects.get(id=request.POST['driver'])
        car = Cars.objects.get(id=request.POST['car'])
        order = Orders.objects.get(id=pk)
        t = Transport.objects.create(driver=driver, car=car)
        t.order.add(order)
        order.status = 2
        order.save()
        return redirect("/")


class ChangeOrderStatusTransportDefined(View):
    def get(self, request, pk):
        order = Orders.objects.get(id=pk)
        order.status = 2
        order.save()
        return redirect('order_detail_view', pk)


class ChangeOrderStatusNew(View):
    def get(self, request, pk):
        order = Orders.objects.get(id=pk)
        order.status = 1
        order.save()
        return redirect('order_detail_view', pk)


class ChangeOrderStatusTransportCancel(View):
    def get(self, request, pk):
        order = Orders.objects.get(id=pk)
        order.status = 4
        order.save()
        return redirect('order_detail_view', pk)


class ChangeOrderStatusTransportDone(View):
    def get(self, request, pk):
        order = Orders.objects.get(id=pk)
        order.status = 3
        order.save()
        return redirect('order_detail_view', pk)


class SettingsView(View, LoginRequiredMixin):
    def get(self, request):
        cars = Cars.objects.all()
        drivers = Drivers.objects.all()
        orders = Orders.objects.all().order_by('delivery_day', 'delivery_hour')
        context = {'cars': cars, 'drivers': drivers, 'orders': orders}
        return render(request, 'settings.html', context)


class FilterOrderView(LoginRequiredMixin, FilterView):
    model = Orders
    template_name = 'order_filter.html'
    filterset_class = OrderFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['Orders'] = Orders.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context
