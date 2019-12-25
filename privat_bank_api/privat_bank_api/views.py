import requests
from django.http import HttpResponse
from django.shortcuts import render

PRIVAT_API = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
try:
    response = requests.get(f'{PRIVAT_API}')
    exchange = response.json()
except requests.ConnectionError:
    raise Exception(
        {"error": f"Unable to connect to PrivatBank api {PRIVAT_API}"}
    )


def health_check(request):
    return HttpResponse("OK")


def index(request):
    return render(request, 'homepage.html')


def usd(request):
    ccy = exchange[0]["ccy"]
    buy = exchange[0]["buy"]
    sale = exchange[0]["sale"]
    return render(request, 'exchange.html', context={"ccy": ccy,
                                                     "buy": buy,
                                                     "sale": sale})


def eur(request):
    ccy = exchange[1]["ccy"]
    buy = exchange[1]["buy"]
    sale = exchange[1]["sale"]
    return render(request, 'exchange.html', context={"ccy": ccy,
                                                     "buy": buy,
                                                     "sale": sale})


def rur(request):
    ccy = exchange[2]["ccy"]
    buy = exchange[2]["buy"]
    sale = exchange[2]["sale"]
    return render(request, 'exchange.html', context={"ccy": ccy,
                                                     "buy": buy,
                                                     "sale": sale})
