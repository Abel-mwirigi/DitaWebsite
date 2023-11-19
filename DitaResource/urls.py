from django.urls import path
from . import views

urlpatterns = [
    path('', views.hardware, name='hardware'),
    path('login/', views.login, name='login'),
]