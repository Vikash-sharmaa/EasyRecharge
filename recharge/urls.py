"""TOPUP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views

urlpatterns = [
   path('mobile/',views.mobile,name='mobileindex'),
   path('dth/',views.dth,name='dthindex'),
   path('datacard/',views.datacard,name='datacardindex'),
   path('metro/',views.metro,name='metroindex'),
   path('payment/',views.payment,name='paymentindex'),
   path('success/',views.success,name='successindex'),
   # TODO path('<int:recharge_id>/',views.mobilerid,name='mobilerid'), In this we want to show history of a partical user
]

