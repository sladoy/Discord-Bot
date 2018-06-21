from system_functions import split_message


def add_filter(message):
    allowed_role = ['458751363849912320', '458714226089918477'] # Admin, Bot
    for role in message.author.roles:
        if role.id in allowed_role:
            filter_word = split_message(message)
            with open ('chat_filter.txt', 'a') as file:
                file.write(filter_word)
                file.write(' ')
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


def create_file():
    f = open('chat_filter.txt', 'a')
    f.close()

