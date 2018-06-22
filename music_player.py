async def music_player(client, message):
    channel = message.author.voice.voice_channel
    voice = await client.join_voice_channel(channel)
    url = message.content.split(' ')
    url = url[-1]
    player = await voice.create_ytdl_player(url)
    player.volume = 0.5
    player.start()