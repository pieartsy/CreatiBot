#discord bot time!
import discord
#imports the palette info
import palette
import os.path
#discord bot token
from config import TOKEN

#defines filepath again
filepath = os.getcwd()

#discord client instance
client = discord.Client()

#when bot boots up, print "Ready!!!!!" to the command line
#the playing status is "$help for both help
@client.event
async def on_ready():
        print("Ready!!!!!")
        await client.change_presence(game=discord.Game(name='$help for bot help'))
@client.event
async def on_message(message):
        if message.content.startswith('$palette'):
                palette.palettegen()
                await client.send_file(message.channel, os.path.join(filepath, "palette.png"))


client.run(TOKEN)