from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('month/', views.monthView),
    path('month/<int:month>/', views.monthView),
    path('week/', views.weekView),
    path('week/<int:week>/', views.weekView),
]

from django.urls import path
from . import views
