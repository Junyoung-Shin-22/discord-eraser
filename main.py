import eraser

TOKEN = ''
with open('./token.txt') as f:
    TOKEN = f.read()

if __name__ == '__main__':
    eraser.ERASER_CLIENT.run(TOKEN)