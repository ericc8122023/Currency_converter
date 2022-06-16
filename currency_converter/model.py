# model.py
# Deals
from ast import ExceptHandler
import requests

# API Call functions
def get_currency_code_map():
     url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
     endpoint = "currencies"
     ext = ".min.json"
     url = url_host + endpoint + ext
     response = requests.get(url_host)

     if response.ok:
          currency_code_map = response.json()
     else:
          currency_code_map = {
      "1inch": "1inch Network",
      "aave": "Aave",
      "ada": "Cardano",
      "aed": "United Arab Emirates Dirham",
      "afn": "Afghan afghani",
      "algo": "Algorand",
      "all": "Albanian lek",
      "amd": "Armenian dram",
      "amp": "Synereo",
      "ang": "Netherlands Antillean Guilder",
      "aoa": "Angolan kwanza",
      "ar": "Arweave",
      "ars": "Argentine peso",
      "atom": "Atomic Coin",
      "aud": "Australian dollar",
      "avax": "Avalanche",


          }
     return response.ok, currency_code_map

def get_exchange_rate(from_code, to_code):
     url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
     endpoint = from_code + "/" + to_code
     ext = ".json"
     url = url_host + endpoint + ext
     response = requests.get(url_host)

     if response.ok:
          exchange = response.json()
          rate = exchange[to_code]
     else:
          rate = 0
     return response.ok, rate



def get_currencies(currency_code_map): 
 currency_strings = []

 for code in currency_code_map.keys():
  currency = currency_code_map[code]
 currency_strings.append(currency + " - " + currency)
 return currency_strings

def get_currency_from_code(code):
     return currency_code_map[code]


def get_currency_string(code):
     return code + " - " + get_currency_from_code(code)


      
success, currency_code_map = get_currency_code_map()
currencies = get_currencies(currency_code_map)
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")

if __name__ == "__main__":
    get_currencies(currency_code_map)
    success, rate = get_exchange_rate("usd" , "eur")
    print(rate)