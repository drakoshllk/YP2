import sqlite3

con = sqlite3.connect("metanit.db")
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE if not exists student
    (
        student_ID INTEGER PRIMARY Key AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        patronymic TEXT NOT NULL,
        group_number INTEGER NOT NULL,
        ratings_ID INTEGER NOT NULL REFERENCES ratings(ratings_ID)
    );
""")


cursor.execute("""DROP TABLE student""")
cursor.close()