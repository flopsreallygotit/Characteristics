# Work Organizer Telegram Bot

Note employee characteristics, follow their progress and achievements!

## Quick Start

1) You will need a token. You can receive it from **@BotFather** in TG with command ```/newbot```

2) Create ```config.env``` file in the root of project:

```config.env
bot_token = None

positions = ["Я учитель", "Я студент"]

protect_content = True 
```

- ```bot_token```: Token that you received from BotFather (Str)
- ```positions```: Positions that bot will assign to user at the start (List of str values)
- ```protect_content```: Toggle forwarding messages (bool: True / False)

In example below all values are default.

3) Complete setup:

For UNIX-like:

```bash
./setup.sh
```

For Windows:

```
pip install aiogram pydantic-settings
```

4) Launch ```main.py```
