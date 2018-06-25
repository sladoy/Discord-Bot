from role_functions import split_message
import discord


class MusicBot:
    def __init__(self, client, message):
        self.channel = message.author.voice.voice_channel
        self.client = client
        self.message = message
        self.url = split_message(message)

    async def start(self):
        try:
            voice = await self.client.join_voice_channel(self.channel)
        except discord.errors.ClientException:
            await MusicBot(self.client, self.message).leave()
            await MusicBot(self.client, self.message).start()
        else:
            song_player = await voice.create_ytdl_player(self.url)
            song_player.volume = 0.4
            song_player.start()

    async def leave(self):
        try:
            server = self.message.server
            voice_client = self.client.voice_client_in(server)
            await voice_client.disconnect()
        except AttributeError:
            await self.client.send_message(self.message.channel, "There's no music")
