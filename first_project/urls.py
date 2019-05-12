"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include # include adds to urlpatterns to specify which route to use
from users import views as user_views



urlpatterns = [ # server looks for patterns that match , where to send
    path('admin/', admin.site.urls), # path to admin page	
    path('register/',user_views.register, name='register'),#if user goes to /register , send them to user_views
    path('', include('blog.urls')), # navigates to blog.urls for further processing/chops off blog part and initializes string that comes after.. ie about
]
