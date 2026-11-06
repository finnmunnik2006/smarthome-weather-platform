import json
import urllib.request
import urllib.error


def huidige_temperatuur_utrecht():
    url = ("https://api.open-meteo.com/v1/forecast"
           "?latitude=52.09&longitude=5.12"
           "&current=temperature_2m&models=knmi_seamless")
    try:
        with urllib.request.urlopen(url, timeout=5) as antwoord:
            data = json.loads(antwoord.read().decode("utf-8"))
        return data["current"]["temperature_2m"]
    except (urllib.error.URLError, KeyError, ValueError, TimeoutError):
        return None