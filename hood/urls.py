from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hood-home'),
    path('systemadmin/', views.systemadmin),
    path('neighbourhoodadmin/', views.neighbourhoodadmin),
    path('client/', views.client),
]