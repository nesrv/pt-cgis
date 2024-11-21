from django.urls import path
# import bookstore.views
from . import views



urlpatterns = [
    path("", views.index),
    path("/about", views.about),
    path("/login", views.login),
    ]