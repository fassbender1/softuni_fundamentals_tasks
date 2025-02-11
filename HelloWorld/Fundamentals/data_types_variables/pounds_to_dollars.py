# UK_pounds = int(input())
#
# pounds_to_dollars = UK_pounds * 1.31
#
# print(f"{pounds_to_dollars :.3f}")

# BGN to GBP with API

import requests

def convert_currencies(currency):

    api_key = '53b7bb339000b9554865a0a5'
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        conversion_rate = data['conversion_rates']['USD']
        dollars = currency * conversion_rate

        return f'{dollars:.3f}'

    else:
        return 'Error fetching exchange rate'

currency_value = int(input())
usd = convert_currencies(currency_value)
print(f'{currency_value} British pounds is equal to {usd} US dollars.')