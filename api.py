import requests


def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=brl,usd&include_24hr_change=true"

    response = requests.request("get", url)
    json = response.json()
    brl_valor = json['cardano']['brl']
    usd_valor = json['cardano']['usd']
    brl_24hr = json['cardano']['brl_24h_change']
    usd_24hr = json['cardano']['usd_24h_change']

    return brl_valor, brl_24hr, usd_valor, usd_24hr
