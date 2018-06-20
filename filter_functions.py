def add_filter(message):
    allowed_role = '458751363849912320' # Admin
    if allowed_role in [role.id for role in message.author.roles]:
        f = message.content.split(' ')
        l_filtra = f[-1]
        with open ('chat_filter.txt', 'a') as file:
            file.write(l_filtra)
            file.write(' ')
        return 'Word {} has been added to filter list'.format(l_filtra)
    else:
        return "You don't have permission to do that."


def rmv_filter(message):
    f = message.content.split(' ')
    remove_word = f[-1]

    allowed_role = '458751363849912320' # Admin

    if allowed_role in [role.id for role in message.author.roles]:
        with open('chat_filter.txt', 'r') as file:
            removal_list = file.readline()
        removal_list = removal_list.split(' ')

        for x in removal_list:
            if x == remove_word:
                removal_list.remove(x)

        with open('chat_filter.txt', 'w') as file:
            file.writelines(removal_list)
    return 'Word has been deleted from filter list'


def create_file():
    f = open('chat_filter.txt', 'a')
    f.close()

