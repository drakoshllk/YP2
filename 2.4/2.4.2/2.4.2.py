# !TASK NOT COMPLETED!

import sqlite3

con = sqlite3.connect("metanit.db")
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE if not exists drink
    (
        drink_ID INTEGER PRIMARY Key AUTOINCREMENT,
        name TEXT NOT NULL,
        strength INTEGER NOT NULL,
        ingredients TEXT NOT NULL
    );
""")

class Drink:
    def __init__(self, name, strength, ingredients):
        self.__name = name
        self.__strength = strength
        self.__ingredients = ingredients
        self.__insert_drink()

    def __insert_drink(self):
        drink_info = [self.__get_name(), self.__get_strength(), self.__get_ingredients()]
        cursor.executemany("INSERT INTO drink (name, strength, ingredients) VALUES (?, ?, ?)", (drink_info,))

    def display_whole_drinks(self):
        cursor.execute("SELECT * FROM drink")
        print(f"                                                     drink\n"
              f"------------------------------------------------------------------------------------------------------------------------")
        for drink in cursor.fetchall():
            print(f"drink_ID:{drink[0]} - name:{drink[1]} - strength:{drink[2]}% - ingredients:{drink[3]}")
        print("------------------------------------------------------------------------------------------------------------------------")


    def __get_name(self):
        return self.__name
    def __get_strength(self):
        return self.__strength
    def __get_ingredients(self):
        return self.__ingredients


drink = Drink("ERSH", 40, "beer, vodka")
drink.display_whole_drinks()
cursor.execute("""DROP TABLE drink""")
cursor.close()