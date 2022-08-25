def _int_readlines(file, comment='#'):
    lines = file.read().splitlines()

    return [int(line.strip()) for line in lines if not line.startswith(comment)]

ADMINS = []
with open('./admins.txt') as f:
    ADMINS = _int_readlines(f)

CHANNELS = []
with open('./channels.txt') as f:
    CHANNELS = _int_readlines(f)

def _check_admin(command):
    async def inner(original_message, *args):
        if original_message.author.id in ADMINS:
            return await command(original_message, *args)
        
        else:
            return
    
    return inner