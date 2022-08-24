from django.urls import path
from . import views

urlpatterns = [
    #name here is an alternateive for the url, cna access by the same name
    path('', views.home, name = "home"),                
    path('room/<str:pk>/', views.rooms, name = "room" ),
]
