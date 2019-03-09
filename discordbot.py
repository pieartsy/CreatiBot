#discord bot time!
import discord
#imports the palette and prompts info
import palette
import prompts
#to join paths
import os
#discord bot token

#discord bot token
TOKEN = os.environ.get('TOKEN')

#defines filepath again
filepath = os.getcwd()

#discord client instance
client = discord.Client()

#help instructions
help_instructions = "- $palette to generate a random palette from colormind.io\n- $prompt to get a random prompt (out of the newest 50) from r/writingprompts"

#when bot boots up, print "Ready!!!!!" to the command line
#the playing status is "$help for both help
@client.event
async def on_ready():
        print("Ready!!!!!")
        game = discord.Game("$help for bot help")
        await client.change_presence(status=discord.Status.idle, activity=game)
#on message $palette, runs palettegen() from the palette.py file, and sends the image to the channel
#where command was sent
@client.event
async def on_message(message):
        if message.content.startswith('$palette'):
                palette.palettegen()
                await message.channel.send(os.path.join(filepath, "palette.png"))
                print("Palette sent!!!!!")
#on message $prompt, runs promptgen from the prompts.py file and sends the prompt the channel
#where command was sent
        if message.content.startswith('$prompt'):
                prompt = prompts.promptgen()
                await message.channel.send(prompt)
                print("Prompt sent!!!!!")
#on message $help, gives help_instructions
        if message.content.startswith('$help'):
                await message.channel.send(help_instructions)
                print("Help sent!!!!!")

#runs the bot
client.run(TOKEN)