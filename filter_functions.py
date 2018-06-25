from role_functions import load_allowed_role, split_message
import json


async def filter_word(client, message):
    try:
        with open('chat_filter.json', 'r') as chat_file:
            chat_filter = json.load(chat_file)

    except (json.decoder.JSONDecodeError, FileNotFoundError):
        with open('chat_filter.json', 'w+') as file:
            json.dump([], file)

    else:
        allowed_role = load_allowed_role()
        for role in message.author.roles:
            if str(role.id) in allowed_role:
                return
        else:
            contents = message.content.split(' ')
            for word in contents:
                if word.upper() in chat_filter:
                    await client.delete_message(message)
                    await client.send_message(message.channel, '**Message was deleted**')


def add_filter(message):
    allowed_role = load_allowed_role()
    for role in message.author.roles:
        if str(role.id) in allowed_role:
            filter_word = split_message(message)
            try:
                with open('chat_filter.json', 'r') as file:
                    data = json.load(file)
            except json.decoder.JSONDecodeError:
                with open('chat_filter.json', 'w+') as file:
                    json.dump([], file)
            else:
                data = list(data)
                data.append(filter_word)

                with open ('chat_filter.json', 'w+') as ex_file:
                    json.dump(data, ex_file)
                return 'Word {} has been added to filter list'.format(filter_word)
    return 'No permissions'


def rmv_filter(message):
    remove_word = split_message(message)

    allowed_role = load_allowed_role()
    for role in message.author.roles:
        if str(role.id) in allowed_role:
            try:
                with open('chat_filter.json', 'r') as file:
                    removal_list = json.load(file)
            except (json.decoder.JSONDecodeError, FileNotFoundError):
                with open('chat_filter.json', 'w+') as file:
                    json.dump([], file)
            else:
                for x in removal_list:
                    if x == remove_word:
                        del_word = remove_word
                try:
                    if del_word:
                        removal_list = list(removal_list)
                        removal_list.remove(del_word)
                except UnboundLocalError:
                    return "Word {} is not on filter list".format(remove_word)
                else:
                    with open('chat_filter.json', 'w+') as file:
                        json.dump(removal_list, file)
                    return 'Word {} has been deleted from filter list'.format(remove_word)
    return 'No permissions'

