from django.urls import path
from pirate.views import list_reestr, reestr_detail

app_name = 'pirate'

urlpatterns = [
    path('', list_reestr ,name='list_reestr'),
    path("reestr-detail/<int:pk>/", reestr_detail, name='reestr_detail'),

]
