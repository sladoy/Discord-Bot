from role_functions import split_message


class MusicBot:
    def __init__(self, client, message):
        self.channel = message.author.voice.voice_channel
        self.client = client
        self.url = split_message(message)
        self.volume = 0.4

    async def start(self):
        voice = await self.client.join_voice_channel(self.channel)
        player = await voice.create_ytdl_player(self.url)
        player.volume = self.volume
        player.start()

    def queue(self, message):
        item_in_queue = split_message(message)





