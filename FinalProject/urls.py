"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from TransportApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='base'),
    path('car/add', views.CarAddView.as_view(), name='car_add_view'),
    path('car/list', views.CarListView.as_view(), name='car_list_view'),
    path('car/delete/<int:pk>', views.CarDeleteView.as_view(), name='car_delete_view'),
    path('driver/add', views.DriverAddView.as_view(), name='driver_add_view'),
    path('driver/list', views.DriverListView.as_view(), name='driver_list_view'),
    path('driver/delete/<int:pk>', views.DriverDeleteView.as_view(), name='driver_delete_view'),
    path('transport/add', views.TransportAddView.as_view(), name='transport_add_view'),
    path('transport/list', views.TransportListView.as_view(), name='transport_list_view'),
    path('transport/delete/<int:pk>', views.TransportDeleteView.as_view(), name='transport_delete_view'),
    path('order/add', views.OrderAddView.as_view(), name='order_add_view'),
    path('order/list', views.OrderListView.as_view(), name='order_list_view'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='order_delete_view'),
]
