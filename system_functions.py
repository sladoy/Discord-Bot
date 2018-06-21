

def allowed_roles_write(message):
    f = split_message(message)
    role_list = [f]
    k = []
    for rola in message.server.roles:
        if str(rola) in role_list:
            k.append(rola.id)

    '''Zrobic zapis do pliku json, ustawic specjalna forme dla tego pliku'''
    return k


def split_message(message):
    splitted_message = message.content.split(' ')
    word = splitted_message[-1]
    return word

