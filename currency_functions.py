import requests
import json


def currencies(message):
    message = message.content.split(' ')
    value_table = []
    curr = message[1]
    try:
        url = 'http://api.nbp.pl/api/exchangerates/rates/c/'+curr.lower()+'/?format=json' # Link do pliku api
        res = requests.get(url)  # uzyskanie wartosci z sieci
        res_dict = res.json() # Uzycie json aby odczytac pobrane wartosci
    except json.decoder.JSONDecodeError:
        return "There's no such currency on the list. Available currencies: " \
               "USD | AUD | CAD | EUR | HUF | CHF | GBP | JPY | CZK | DKK | " \
               "NOK | SEK | XDR"
    else:
        rep_dicts = res_dict['rates'] # Uzyskanie dostepu do elementow w zakladce 'rates'
        rep_elements = rep_dicts[0] # Wybranie grupy elementow

        for x in rep_elements.values():
            value_table.append(x) # Przypisanie elementow do tablicy
        bid = value_table[-2] # Przypisanie wartosci z tablicy
        ask = value_table[-1]
        date = value_table[-3]

        msg = 'Value ' + curr.upper() + ' to PLN | Date: {}  Bid: {} Ask: {}'.format(date, bid, ask)

        if len(message) == 2:
            return msg
        else:
            value = ' | Value '+curr.upper()+' to PLN | '
            curr = float(message[-1])
            result = round(bid * curr, 4)
            value += str(result)
            return msg + value


