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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import PasswordResetView, PasswordChangeView  #function based are remove and class based are using now for reseting the password as well as changing the password!!...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
    path('register/',include('register.urls')),
    path('',include('home.urls')),
    path('recharge/',include('recharge.urls')),
    path('password_reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password_change/',PasswordChangeView.as_view(),name='password_change'),  #for password Changing after the user is loggined..
    path('', include('django.contrib.auth.urls')),   #necessary for reset password and gives error of "Reverse for 'password_reset_confirm' not found. 'password_reset_confirm' is not a valid view function or pattern name"





] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
