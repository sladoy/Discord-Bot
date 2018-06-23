import requests


def eur():
    value_table = []
    url = 'http://api.nbp.pl/api/exchangerates/rates/c/eur/?format=json' # Link do pliku api
    res = requests.get(url) # uzyskanie wartosci z sieci
    res_dict = res.json() # Uzycie json aby odczytac pobrane wartosci
    rep_dicts = res_dict['rates'] # Uzyskanie dostepu do elementow w zakladce 'rates'
    rep_elements = rep_dicts[0] # Wybranie grupy elementow

    for x in rep_elements.values():
        value_table.append(x) # Przypisanie elementow do tablicy
    bid = value_table[-2] # Przypisanie wartosci z tablicy
    ask = value_table[-1]
    date = value_table[-3]
    msg = 'Value EUR to PLN | Date: {}  Bid: {} Ask: {}'.format (date, bid, ask)
    return msg


def usd():
    value_table = []
    url = 'http://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json' # Link do pliku api
    res = requests.get(url) # uzyskanie wartosci z sieci
    res_dict = res.json() # Uzycie json aby odczytac pobrane wartosci
    rep_dicts = res_dict['rates'] # Uzyskanie dostepu do elementow w zakladce 'rates'
    rep_elements = rep_dicts[0] # Wybranie grupy elementow

    for x in rep_elements.values():
        value_table.append(x) # Przypisanie elementow do tablicy
    bid = value_table[-2] # Przypisanie wartosci z tablicy
    ask = value_table[-1]
    date = value_table[-3]
    msg = 'Value USD to PLN | Date: {}  Bid: {} Ask: {}'.format(date, bid, ask)
    return msg


def gbp():
    value_table = []
    url = 'http://api.nbp.pl/api/exchangerates/rates/c/gbp/?format=json' # Link do pliku api
    res = requests.get(url) # uzyskanie wartosci z sieci
    res_dict = res.json() # Uzycie json aby odczytac pobrane wartosci
    rep_dicts = res_dict['rates'] # Uzyskanie dostepu do elementow w zakladce 'rates'
    rep_elements = rep_dicts[0] # Wybranie grupy elementow

    for x in rep_elements.values():
        value_table.append(x) # Przypisanie elementow do tablicy
    bid = value_table[-2] # Przypisanie wartosci z tablicy
    ask = value_table[-1]
    date = value_table[-3]
    msg = 'Value GBP to PLN | Date: {}  Bid: {} Ask: {}'.format(date, bid, ask)
    return msg


def count_waluta():
    pass