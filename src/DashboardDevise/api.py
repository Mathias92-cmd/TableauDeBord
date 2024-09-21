from datetime import date , timedelta
from pprint import pprint

import requests

def get_rates(currencies , days=30):
    endDate = date.today()
    startDate = endDate - timedelta(days=days)

    symbols = ','.join(currencies)
    requete = f"https://www.docstring.fr/api/rates/history/?start_at={startDate}&end_at={endDate}&symbols={symbols}"
    r = requests.get(requete)
    if not r and not r.json():
        return False, False

    apiRates = r.json().get("rates")

    allRates = {currency: [] for currency in currencies}
    allDays = (sorted(apiRates.keys()))

    for eachDay in allDays:
        [allRates[currency].append(rate) for currency, rate in apiRates[eachDay].items()]
    return allDays , allRates


    return None, None


if __name__ == '__main__':
    days , rates = get_rates(currencies=["USD" , "CAD"])
    pprint(days)
    pprint(rates)