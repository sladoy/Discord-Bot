from currency_functions import currencies
from music_player import MusicBot
from filter_functions import filter_word, add_filter, rmv_filter
from role_functions import write_allowed_roles, show_my_id_role, delete_allowed_role
from help import command_help


async def messages(client, message):

    await filter_word (client, message)

    if message.content.startswith ('?hello'):
        msg = 'Hello, {0.author.mention}'.format (message)
        await client.send_message (message.channel, msg)

    elif message.content.startswith ('?bot'):
        msg = 'My solemnly purpose is to serve you my Master'
        await client.send_message (message.channel, msg)

    elif message.content.startswith('?curr'):
        await client.send_message(message.channel, currencies(message))

    elif message.content.startswith('?add_filter'):
        await client.send_message(message.channel, add_filter(message))

    elif message.content.startswith('?rmv_filter'):
        await client.send_message (message.channel, rmv_filter(message))

    elif message.content.startswith('?play'):
        await MusicBot(client, message).start()

    elif message.content.startswith('?allow'):
        await client.send_message (message.channel, write_allowed_roles(message))

    elif message.content.startswith('?deny'):
        await client.send_message(message.channel, delete_allowed_role(message))

    elif message.content.startswith('?show'):
        await client.send_message(message.channel, show_my_id_role(message))

    elif message.content.startswith('?help'):
        await client.send_message(message.channel, command_help())

