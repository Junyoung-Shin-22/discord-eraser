import discord
import commands
import utils

import asyncio

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

    content = message.content
    if not content:
        content = "?"

    command, *args = content.split()

    if command in commands.COMMANDS:
        try:
            # always delete command messages first
            await message.delete()
            if not message.author.bot:
                await commands.COMMANDS[command](message, *args)
        except:
            pass
    else: # any message in listening channels should be deleted
        await asyncio.sleep(3600)
        try:
            await message.delete()
        except:
            pass