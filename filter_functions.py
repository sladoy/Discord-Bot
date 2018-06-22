
def split_message(message):
    splitted_message = message.content.split(' ')
    word = splitted_message[-1]
    return word


async def filter_word(client, message):
    f = open('chat_filter.txt', 'a')
    f.close()
    with open('chat_filter.txt', 'r') as chat_file:
        chat_filter = chat_file.read()
        chat_filter = chat_filter.split(' ')
    allowed_role = ['458751363849912320', '458714226089918477'] # Admin, Bot
    for role in message.author.roles:
        if role.id in allowed_role:
            return
    else:
        contents = message.content.split (" ")
        for word in contents:
            if word.upper() in chat_filter:
                await client.delete_message(message)
                await client.send_message(message.channel, '**Message was deleted**')


def add_filter(message):
    allowed_role = ['458751363849912320', '458714226089918477'] # Admin, Bot
    for role in message.author.roles:
        if role.id in allowed_role:
            filter_word = split_message(message)
            with open ('chat_filter.txt', 'a') as file:
                file.write(filter_word + ' ')
            return 'Word {} has been added to filter list'.format(filter_word)
    return 'No permissions'


def rmv_filter(message):
    remove_word = split_message(message)

    allowed_role = ['458751363849912320', '458714226089918477'] # Admin, Bot
    for role in message.author.roles:
        if role.id in allowed_role:
            with open('chat_filter.txt', 'r') as file:
                removal_list = file.readline()
            removal_list = removal_list.split(' ')

            for x in removal_list:
                if x == remove_word:
                    removal_list.remove(x)

            with open('chat_filter.txt', 'w') as file:
                file.writelines(removal_list)
            return 'Word {} has been deleted from filter list'.format(remove_word)
    return 'No permissions'

