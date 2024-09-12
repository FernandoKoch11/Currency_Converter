import requests

def converter_currency(currency_origin, destination_currency):
    link = f'https://economia.awesomeapi.com.br/last/{currency_origin}-{destination_currency}'
    request = requests.get(link)
    
    quot = request.json()[f'{currency_origin}{destination_currency}']['bid']
    return quot
