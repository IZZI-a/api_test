import requests
from django.shortcuts import render


def gog_list(request):
    response = requests.get("https://hydralinks.cloud/sources/gog.json")
    data = response.json()

    gog = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"gog": gog})


def atopgames_list(request):
    response = requests.get("https://hydralinks.cloud/sources/atop-games.json")
    data = response.json()

    atopgames = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"atopgames": atopgames})


def steamsoft_list(request):
    response = requests.get("https://hydralinks.cloud/sources/steamrip-software.json")
    data = response.json()

    steamsoft = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"steamsoft": steamsoft})


def steamrip_list(request):
    response = requests.get("https://hydralinks.cloud/sources/steamrip.json")
    data = response.json()

    steamrip = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"steamrip": steamrip})


def dodi_list(request):
    response = requests.get("https://hydralinks.cloud/sources/dodi.json")
    data = response.json()

    dodi = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"dodi": dodi})


def empress_list(request):
    response = requests.get("https://hydralinks.cloud/sources/empress.json")
    data = response.json()

    empress = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"empress": empress})


def fitgirl_list(request):
    response = requests.get("https://hydralinks.cloud/sources/fitgirl.json")
    data = response.json()

    fitgirl = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"fitgirl": fitgirl})


def kaoskrew_list(request):
    response = requests.get("https://hydralinks.cloud/sources/kaoskrew.json")
    data = response.json()

    kaoskrew = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"kaoskrew": kaoskrew})


def onlinefix_list(request):
    response = requests.get("https://hydralinks.cloud/sources/onlinefix.json")
    data = response.json()

    onlinefix = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"onlinefix": onlinefix})


def tinyrepacks_list(request):
    response = requests.get("https://hydralinks.cloud/sources/tinyrepacks.json")
    data = response.json()

    tinyrepacks = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"tinyrepacks": tinyrepacks})


def xatab_list(request):
    response = requests.get("https://hydralinks.cloud/sources/xatab.json")
    data = response.json()

    xatab = data.get("downloads", [])
    return render(request, "pirate/pirate_list.html", {"tinyrepacks": xatab})
