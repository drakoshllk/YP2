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
cursor.execute("""
    CREATE TABLE if not exists ratings
    (
        ratings_ID INTEGER PRIMARY Key AUTOINCREMENT,
        rating_first INTEGER NOT NULL,
        rating_second INTEGER NOT NULL,
        rating_third INTEGER NOT NULL,
        rating_fourth INTEGER NOT NULL
    );
""")
counter = 1
class Student:
    def __init__(self, name, surname, patronymic, group_number, ratings, ratings_ID): # ratings 4 elem arr
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__group_number = group_number
        self.__ratings = ratings
        self.__ratings_ID = ratings_ID
        self.__insert_student()

    def __insert_student(self):
        student_info = [self.__get_name(), self.__get_surname(), self.__get_patronymic(), self.__get_group_number(), self.__ratings_ID]
        cursor.executemany("INSERT INTO student (name, surname, patronymic, group_number, ratings_ID) VALUES (?, ?, ?, ?, ?)", (student_info,))
        cursor.executemany("INSERT INTO ratings (rating_first, rating_second, rating_third, rating_fourth) VALUES (?, ?, ?, ?)",(self.__get_ratings(),))


    def __get_name(self):
        return self.__name
    def __get_surname(self):
        return self.__surname
    def __get_patronymic(self):
        return self.__patronymic
    def __get_group_number(self):
        return self.__group_number
    def __get_ratings(self):
        return self.__ratings

    def display_whole_info(self):
        cursor.execute("SELECT * FROM student")
        for person in cursor.fetchall():
            print(f"{person[0]} - {person[1]} - {person[2]} - {person[3]} - {person[4]} - {person[5]}")
        print()
        cursor.execute("SELECT * FROM ratings")
        for rating in cursor.fetchall():
            print(f"{rating[0]} - {rating[1]} - {rating[2]} - {rating[3]} - {rating[4]}")



student = Student("Anton", "Litvinov", "Dmitryevich", 643, [3, 3, 4, 5], 1)
student1 = Student("Anton", "Litvinov", "Dmitryevich", 643, [5, 5, 5, 5], 2)
student.display_whole_info()
cursor.execute("""DROP TABLE student""")
cursor.execute("""DROP TABLE ratings""")
cursor.close()