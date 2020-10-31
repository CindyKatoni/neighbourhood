from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('systemadmin/', views.systemadmin),
    path('neighbourhoodadmin/', views.neighbourhoodadmin),
]