import discord
from system_functions import messages


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


@client.event
async def on_message(message):
    await messages(client, message)


client.run('NDU4MDMzMDg4Nzc4NDY5Mzc2.DghwEw.9fGYGoSysCbQzlHXVftLKJBWRuU')
