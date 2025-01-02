import requests
from django.shortcuts import render

def pirate_list(request):
    response = requests.get('https://hydralinks.cloud/sources/gog.json')
    data = response.json()

    downloads = data.get('downloads', [])
    return render(request, 'pirate/pirate_list.html', {'downloads': downloads})

