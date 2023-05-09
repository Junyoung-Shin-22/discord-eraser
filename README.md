# discord-eraser 1.0.0

## 1. Requirements
```
pip install discord==1.7.3
```

Also, three `.txt` files named `token.txt`, `admins.txt`, `channels.txt` have to be manually added.
* `token.txt` Bot token
* `admins.txt` IDs of admin users who can use `.?`(purge) command (at each line)
* `channels.txt` IDs of text channels for the bot to be activated (at each line)

## 2. Usage
```
$ . run.sh
```

## 3. bot commands
* `.` delete most recent message of the user in the channel
* `..` delete all messages of the user in the channel
* `.?` (admins only) purge; delete all messages in the channel
