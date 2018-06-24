from role_functions import split_message


ytdl_format_options = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': True,
    'logtostderr': False,
    'quiet': True,
    'verbose': False,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}


class MusicBot:
    def __init__(self, client, message):
        self.channel = message.author.voice.voice_channel
        self.client = client
        self.url = split_message(message)
        self.queue = []

    async def start(self):
        voice = await self.client.join_voice_channel(self.channel)
        song_player = await voice.create_ytdl_player(self.url, ytdl_options=ytdl_format_options)
        song_player.volume = 0.4
        song_player.start()












