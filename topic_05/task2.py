import requests

url = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
source = url.json()


currency_rates = {}
for rate in source:
    currency_rates[rate['cc']] = rate['rate']


supported_currencies = ["EUR", "USD", "PLN"]


while True:
    currency = input("Enter the currency (EUR, USD, PLN): ").upper()
    if currency not in supported_currencies:
        print("This currency is not supported.")
    else:
        break

amount = float(input("Enter the amount of currency: "))


converted_amount = amount * currency_rates[currency]


print(f"{amount} {currency} = {converted_amount} ₴")