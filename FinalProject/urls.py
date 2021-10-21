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
from django.urls import path, include
from TransportApp import views
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='base'),
    path('car/add', views.CarAddView.as_view(), name='car_add_view'),
    path('car/list', views.CarListView.as_view(), name='car_list_view'),
    path('car/delete/<int:pk>', views.CarDeleteView.as_view(), name='car_delete_view'),
    path('car/modify/<int:pk>', views.CarUpdateView.as_view(), name='car_modify_view'),
    path('car/detail/<int:pk>', views.CarDetailView.as_view(), name='car_detail_view'),
    path('driver/add', views.DriverAddView.as_view(), name='driver_add_view'),
    path('driver/list', views.DriverListView.as_view(), name='driver_list_view'),
    path('driver/delete/<int:pk>', views.DriverDeleteView.as_view(), name='driver_delete_view'),
    path('driver/modify/<int:pk>', views.DriverUpdateView.as_view(), name='driver_update_view'),
    path('driver/detail/<int:pk>', views.DriverDetailView.as_view(), name='driver_detail_view'),
    path('transport/add', views.TransportAddView.as_view(), name='transport_add_view'),
    path('transport/list', views.TransportListView.as_view(), name='transport_list_view'),
    path('transport/delete/<int:pk>', views.TransportDeleteView.as_view(), name='transport_delete_view'),
    path('transport/modify/<int:pk>', views.TransportUpdateView.as_view(), name='transport_update_view'),
    path('transport/detail/<int:pk>', views.TransportDetailView.as_view(), name='transport_detail_view'),
    path('order/add', views.OrderAddView.as_view(), name='order_add_view'),
    path('order/list', views.OrderListView.as_view(), name='order_list_view'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='order_delete_view'),
    path('order/detail/<int:pk>', views.DetailOrderView.as_view(), name='order_detail_view'),
    path('order/modify/<int:pk>', views.OrderUpdateView.as_view(), name='order_update_view'),
    path('accounts/login/', v.LoginView.as_view(), name='login'),
    path('register/', v.RegisterView.as_view(), name='register'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
    path('order/detail/<int:pk>/status/2', views.ChangeOrderStatusTransportDefined.as_view(), name='TransportDefined'),
    path('order/detail/<int:pk>/status/1', views.ChangeOrderStatusNew.as_view(), name='NewOrder'),
    path('order/detail/<int:pk>/status/3', views.ChangeOrderStatusTransportDone.as_view(), name='DoneOrder'),
    path('order/detail/<int:pk>/status/4', views.ChangeOrderStatusTransportCancel.as_view(), name='CancelOrder'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('order/filter/', views.FilterOrderView.as_view(), name='order_filter')

]
