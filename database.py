import json

from config import bot_config

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Database:
    __data = {}

    def __init__(self, filename: str):
        self.__filename = filename

        try:
            with open(filename, "r") as db_file:
                try:
                    self.__data = json.load(db_file)
                    print(f"Read data from db `{filename}`")

                except ValueError:
                    print(f"Db `{filename}` is empty or incorrect. Assigned null to data.")

        except FileNotFoundError:
            print(f"Db `{filename}` doesn't exist. Created it.")
                  
            with open(filename, "x") as db_file:
                pass

    def change_characteristic(self, username: str, characteristic: str, value) -> None:
        self.__data[username] = {characteristic: value}

    def receive_characteristics(self, username: str) -> str:
        return json.dumps(self.__data[username])
    
    def save_database(self):
        with open(self.__filename, "w") as db_file:
            json.dump(self.__data, db_file)

    def __del__(self):
        self.save_database()

db = Database(bot_config.db_filename)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
