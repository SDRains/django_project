from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('administration/', views.administration, name="administration"),
]
