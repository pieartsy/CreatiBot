#discord bot time!
import discord
#imports the palette info
import palette
import os.path

filepath = "C:\\Users\\Maddie\\Pictures\\palettes"

#old token, the new one has been regenerated and is not on git
TOKEN = ""
client = discord.Client()

@client.event
async def on_ready():
        print("Ready!!!!!")

@client.event
async def on_message(message):
        if message.content.startswith('$palette'):
                palette.palettegen()
                await client.send_file(message.channel, os.path.join(filepath, "palette.png"))

client.run(TOKEN)