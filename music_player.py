from role_functions import split_message


class MusicBot:
    def __init__(self, client, message):
        self.channel = message.author.voice.voice_channel
        self.client = client
        self.url = split_message(message)
        self.queue = []

    async def start(self):
        voice = await self.client.join_voice_channel(self.channel)
        song_player = await voice.create_ytdl_player(self.url)
        song_player.volume = 0.4
        song_player.start()












