import discord
import commands
import utils

_ALL_INTENTS = discord.Intents.all()
ERASER_CLIENT = discord.Client(intents=_ALL_INTENTS)

@ERASER_CLIENT.event
async def on_ready():
    print('We have logged in as {0.user}'.format(ERASER_CLIENT))

@ERASER_CLIENT.event
async def on_message(message):

    # ignore messages from unregistered channels
    if message.channel.id not in utils.CHANNELS:
        return

    # ignore messages from the bot itself
    if message.author.id != ERASER_CLIENT.user.id:
        content = message.content
        if not content:
            return

        command, *args = content.split()

        if command in commands.COMMANDS:
            try:
                # always delete command messages first
                await message.delete()
                await commands.COMMANDS[command](message, *args)
            except:
                pass