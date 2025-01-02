from django.urls import path
from pirate.views import pirate_list

app_name = 'pirate'

urlpatterns = [
    path('', pirate_list, name='pirate_list'),
]
