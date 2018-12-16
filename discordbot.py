#discord bot time!
import discord
#imports the palette info
import palette
import os.path
from config import TOKEN

filepath = os.getcwd()

client = discord.Client()

@client.event
async def on_ready():
        print("Ready!!!!!")
        await client.change_presence(game=discord.Game(name='$palette for random palette!'))
@client.event
async def on_message(message):
        if message.content.startswith('$palette'):
                palette.palettegen()
                await client.send_file(message.channel, os.path.join(filepath, "palette.png"))

client.run(TOKEN)