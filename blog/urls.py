# following structure of base/urls module I named [first_project]
# map url pattern to view function
from django.urls import path
# import views.py within our url /(.) == Current Directory
from . import views

# (path, view to handle logic for route, name of path)
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
]