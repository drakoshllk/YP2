import sqlite3
import random

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
        student_info = [self.__get_name(), self.__get_surname(), self.__get_patronymic(), self.__get_group_number(), self.__get_ratings_ID()]
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
    def __get_ratings_ID(self):
        return self.__ratings_ID


    def display_whole_tables(self):
        cursor.execute("SELECT * FROM student")
        print(f"                                                     STUDENT"
              f"\n------------------------------------------------------------------------------------------------------------------------")
        for person in cursor.fetchall():
            print(f"student_ID:{person[0]} - name:{person[1]} - surname:{person[2]} - patronymic:{person[3]} - group_number:{person[4]} - ratings_ID:{person[5]}")
        print("------------------------------------------------------------------------------------------------------------------------")
        cursor.execute("SELECT * FROM ratings")
        print(f"                                                     RATINGS"
              f"\n------------------------------------------------------------------------------------------------------------------------")
        for rating in cursor.fetchall():
            print(f"PK:{rating[0]} - {rating[1]} - {rating[2]} - {rating[3]} - {rating[4]}")

    def display_student_info(self, student_ID):
        cursor.execute(f"SELECT * FROM student WHERE student_ID={student_ID}")
        student_ID, name, surname, patronymic, group_number, ratings_ID = cursor.fetchone()
        print(f"                                                     STUDENT"
              f"\n------------------------------------------------------------------------------------------------------------------------")
        print(
            f"student_ID:{student_ID} - name:{name} - surname:{surname} - patronymic:{patronymic} - group_number:{group_number} - ratings_ID:{ratings_ID}")
        print("------------------------------------------------------------------------------------------------------------------------")
        cursor.execute(f"SELECT * FROM ratings WHERE ratings_ID={ratings_ID}")
        rating_first, rating_second, rating_third, rating_fourth = cursor.fetchone()[1:]
        print(f"                                                     RATINGS"
              f"\n------------------------------------------------------------------------------------------------------------------------")
        print(f"PK:{ratings_ID} - {rating_first} - {rating_second} - {rating_third} - {rating_fourth}")

    def update_student(self, parameter, value, student_ID):
        cursor.execute(f"UPDATE student SET {parameter} = '{value}' WHERE student_ID='{student_ID}'")

    def delete_student(self, student_ID):
        cursor.execute(f"DELETE FROM student WHERE student_ID={student_ID}")

    def display_AVG_group_rating(self, group_number):
        cursor.execute(f"SELECT ratings_ID FROM student WHERE group_number={group_number}")
        target_ratings_ID = []
        for num in cursor.fetchall():
            target_ratings_ID.append(num[0])
        AVG_rating = []
        for i in range(len(target_ratings_ID)):
            cursor.execute(f"SELECT * FROM ratings WHERE ratings_ID={target_ratings_ID[i]}")
            rating_first, rating_second, rating_third, rating_fourth = cursor.fetchone()[1:]
            AVG_temp = [rating_first, rating_second, rating_third, rating_fourth]
            AVG = sum(AVG_temp) / len(AVG_temp)
            AVG_rating.append(AVG)
        print(AVG_rating)
        AVG_group_rating = sum(AVG_rating) / len(AVG_rating)
        print(AVG_group_rating)
# students = []
# students1 = []
#
# for i in range(1, 11):
#     rnd1, rnd2, rnd3, rnd4 = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
#     students.append(Student("Anton", "Litvinov", "Dmitryevich", 643, [rnd1, rnd2, rnd3, rnd4], i))
#
# for i in range(11, 22):
#     rnd1, rnd2, rnd3, rnd4 = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
#     students1.append(Student("bob", "aaron", "jakevich", 641, [rnd1, rnd2, rnd3, rnd4], i))
#
# # student = Student("Anton", "Litvinov", "Dmitryevich", 643, [3, 3, 4, 5], 1)
# # student1 = Student("bob", "aaron", "jakevich", 641, [5, 5, 5, 5], 2)
# # students[0].display_whole_tables()
# students[0].display_AVG_group_rating(643)
# # student.display_student_info(2)
# cursor.execute("""DROP TABLE student""")
# cursor.execute("""DROP TABLE ratings""")
# cursor.close()





