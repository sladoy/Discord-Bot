import discord
from currency_functions import eur, usd
from filter_functions import add_filter, rmv_filter, create_file
from discord.ext.commands import Bot


Client = discord.Client( )
BOT_PREFIX = '?'
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print("Ready to duty")
    print(client.user.name)
    print(client.user.id)
    print('-------------')

# ------------ Filtering Words ---------------------------


@client.event
async def filter_word(message):
    create_file()
    with open('chat_filter.txt', 'r') as chat_file:
        chat_filter = chat_file.read()
        chat_filter = chat_filter.split(' ')
    '''Problem jest z tablica stringow. Moze odczytywac wartosci rol z pliku? Wczesniej zapisujac wartosci
    rol do pliku?'''
    allowed_role = '458751363849912320' # Admin
    if allowed_role in [role.id for role in message.author.roles]:
        return
    else:
        contents = message.content.split (" ")  # Dzieli zdanie na slowa
        for word in contents:
            if word.upper ( ) in chat_filter:
                await client.delete_message(message)
                await client.send_message(message.channel, '**Message was deleted**')
# ------------------------------------------------------------

# --------------Music Player----------------------------------


@client.event
async def music_player(message):
    channel = message.author.voice.voice_channel
    voice = await client.join_voice_channel(channel)
    url = message.content.split(' ')
    url = url[-1]
    player = await voice.create_ytdl_player(url)
    player.start ( )

# -------------------------------------------------------------


@client.event
async def on_message(message):
    await filter_word (message)
    client.process_commands (message)
    if message.content.startswith ('?hello'):
        msg = 'Hello, {0.author.mention}'.format (message)
        await client.send_message (message.channel, msg)
    elif message.content.startswith ('?bot'):
        msg = 'My solemnly purpose is to serve you my Master'
        await client.send_message (message.channel, msg)
    elif message.content.startswith('?usd'):
        await client.send_message (message.channel, usd())
    elif message.content.startswith('?eur'):
        await client.send_message (message.channel, eur())
    elif message.content.startswith('?add_filter'):
        await client.send_message(message.channel, add_filter(message))
    elif message.content.startswith('?rmv_filter'):
        await client.send_message (message.channel, rmv_filter(message))
    elif message.content.startswith('?play'):
        await music_player(message)
    elif message.content.startswith('?stop'):
        pass

client.run('NDU4MDMzMDg4Nzc4NDY5Mzc2.DghwEw.9fGYGoSysCbQzlHXVftLKJBWRuU')
