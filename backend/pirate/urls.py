from django.urls import path
from pirate.views import gog_list

app_name = 'pirate'

urlpatterns = [
    path('', gog_list ,name='gog_list'),
]
