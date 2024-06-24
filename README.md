# Characteristics

Do you want to know what people think about you? Or maybe you want to leave a review about someone? Then this bot is perfect for you. Only 2 commands that can change or show a person's current characteristics. It's time to become a real favorite or transform into a real villain.

## Usage

- ```/start```: Displays info about bot
- ```/add <username> <characteristic> <value>```: Adds characteristic to user
- ```/show <username>```: Shows characteristics of user

## Quick Start

1) You will need a token. You can receive it from **@BotFather** in TG with command ```/newbot```

2) Create ```config.env``` file in the root of project:

```config.env
token = None

db_filename = "users.json"

protect_content = True 
```

- ```token```: Token that you received from BotFather (Str)
- ```db_filename```: Filename of database (Str)
- ```protect_content```: Toggle forwarding messages (bool: True / False)

In example below all values are default.

3) Complete setup and launch bot:

```bash
./setup.sh
python3 main.py
```
