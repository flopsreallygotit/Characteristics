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

max_query_count = 5

db_filename = "users.json"

protect_content = False 
```

- ```token```: Token that you received from BotFather (Str)
- ```max_query_count```: The number of requests after which the database will be flushed to the hard drive
- ```db_filename```: Filename of database (Str)
- ```protect_content```: Toggle forwarding messages (bool: True / False)

In example below all values are default.

3) Complete setup and launch bot:

```bash
./setup.sh
python3 main.py
```

### Database format

```json
{
    "Flops": [
        {"Stamina": "6"},
        {"Strength": "5"},
        {"Health": "7"},
        {"Name": "Secret"}
    ],
    "OncomingLane": [
        {"Stamina": "5"},
        {"Strength": "6"},
        {"Hobby": "Car_repair_works"}
    ],
    "AlexeyOsipov742": [
        {"Health": "0"},
        {"Hobby": "OncomingLane"}
    ]
}
```