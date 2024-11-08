from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('year/<int:year_id>/', views.get_year),
    path('<str:book_name>/', views.get_book),


]