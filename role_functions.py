from filter_functions import split_message
import json


def write_allowed_roles(message):
    f = split_message(message)
    role_list = [f]
    k = []
    for rola in message.server.roles:
        if str(rola) in role_list:
            k.append(rola.id)
    dictionary = dict(zip(role_list, k))

    with open('roles.json', '+w') as file:
        json.dump(dictionary, file)
    '''Zrobic zapis do pliku json, ustawic specjalna forme dla tego pliku'''
    return k


def show_my_id_role(message):
    '''Funkcja bedzie pokazywala moja role oraz jej id'''
    rola = message.author.roles # Dostanie adresow ról w pamieci
    l = {} # puste directory
    for role in message.server.roles:
        if role in rola:
            l[role] = [role.id]

    return l

