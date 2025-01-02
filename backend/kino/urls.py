from django.urls import path
from kino import views

app_name = 'kino'

urlpatterns = [
    path('', views.base, name='home'),
]
