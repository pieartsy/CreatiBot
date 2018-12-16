#discord bot time!
import discord
#imports the palette and prompts info
import palette
import prompts
#to join paths
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
#on message $palette, runs palettegen() from the palette.py file, and sends the image to the channel
#where command was sent
@client.event
async def on_message(message):
        if message.content.startswith('$palette'):
                palette.palettegen()
                await client.send_file(message.channel, os.path.join(filepath, "palette.png"))
#on message $prompt, runs promptgen from the prompts.py file and sends the prompt the channel
#where command was sent
@client.event
async def on_message(message):
        if message.content.startswith('$prompt'):
                prompt = prompts.promptgen()
                await client.send_message(message.channel, prompt)

#runs the bot
client.run(TOKEN)