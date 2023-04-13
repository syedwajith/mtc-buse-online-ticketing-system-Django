"""mtc_bus_ticketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from mtc_bus_ticketing_app import views

urlpatterns = [
    path('', views.index),
    path('adminlogin/', views.adminlogin),
    path('adminhome/', views.adminhome),
    path('addbus/', views.addbus),
    path('busroutes/', views.busroutes),
    path('routedetails/', views.routedetails),
    path('updatebus1/', views.updatebus1),
    path('updatebus2/', views.updatebus2),
    path('updatebus2_update/<int:id>/', views.updatebus2_update),
    path('updatebus3/', views.updatebus3),
    path('deletebus/', views.deletebus),
    path('todaycollection/', views.todaycollection),
    path('overallcollection/', views.overallcollection),
    path('viewbusroutes/', views.viewbusroutes),
]
