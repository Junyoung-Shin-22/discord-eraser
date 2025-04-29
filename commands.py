import utils

async def _delete_one(original_message, *args):
    if args:
        return

    channel = original_message.channel
    author = original_message.author

    async for message in channel.history(limit=None):
        if message.author.id == author.id:
            await message.delete()
            break

async def _delete_all(original_message, *args):
    if args:
        return
    
    channel = original_message.channel
    author = original_message.author

    messages = []

    async for message in channel.history(limit=None):
        if message.author.id ==author.id:
            messages.append(message)
    
    for i in range(0, len(messages), 100):
        await channel.delete_messages(messages[i: i+100])

# @utils._check_admin
async def _purge(original_message, *args):
    if args:
        return
    
    channel = original_message.channel
    await channel.purge(limit=None)

COMMANDS =\
    {
        '.':
            _delete_one,
        
        '..':
            _delete_all,
        
        '.?':
            _purge,
    }