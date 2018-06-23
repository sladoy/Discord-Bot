import json


def split_message(message):
    splitted_message = message.content.split(' ')
    word = splitted_message[-1]
    return word


def write_allowed_roles(message):
    '''Funkcja tworzy i zapisuje nazwe i id ról'''
    word = split_message(message)
    role_list = word
    try:
        with open('roles.json', 'r') as file:
            data = json.load(file)

    except json.decoder.JSONDecodeError:
        with open('roles.json', 'w+') as file:
            json.dump({}, file)

        dict_role = {}

        for role in message.server.roles:
            if str(role) in str(role_list):
                dict_role[role_list] = str(role.id)

        with open('roles.json', 'w+') as ex_file:
            json.dump(dict_role, ex_file)

    else:
        for role in message.server.roles:
            if str(role) in str(role_list):
                data[role_list] = str(role.id)

        with open('roles.json', 'w+') as ex_file:
            json.dump(data, ex_file)

    return 'Role is added to the allowed roles'


def load_allowed_role():
    '''Funkcja wykorzystywana jest do ladowania id uzytkownikow.
        Wykorzystywana jest w funkcjach filtrujacacyh'''
    value_list = []
    try:
        with open('roles.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        with open('roles.json', 'w+') as file:
            json.dump({}, file)
    else:
        for value in data.values():
            value_list.append(value)

    return value_list


def delete_allowed_role(message):
    word = split_message(message)
    try:
        with open('roles.json', 'r') as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        with open('roles.json', 'w+') as file:
            json.dump({}, file)
    else:
        for role in message.server.roles:
            if str(role) in str(word):
                del_id = str(role.id)

        for k, v in data.items():
            if k == word and v == del_id:
                del_key = word
        try:
            if del_key:
                del data[del_key]
                with open('roles.json', 'w+') as file:
                    json.dump(data, file)
            return 'Role has been deleted from allowed roles'
        except UnboundLocalError:
            return "Role can't be find"


def show_my_id_role(message):
    role_list = {}

    for role in message.server.roles:
        if message.author.top_role in message.server.roles:
            role_list[str(message.author.top_role)] = [str(message.author.top_role.id)]

    return role_list


