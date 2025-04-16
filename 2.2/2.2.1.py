class Student:
    def __init__(self, surname, DOB, group_number, academic_performance): # academic_performance - 5 elem arr
        self.__surname = surname
        self.__DOB = DOB
        self.__group_number = group_number
        self.academic_performance = academic_performance

    def display_info(self):
        print(f'student surname: {self.get_surname()}\n'
              f'student date of birthday: {self.get_DOB()}\n')

    def get_surname(self):
        return self.__surname
    def set_surname(self, surname):
        self.__surname = surname

    def get_DOB(self):
        return self.__DOB
    def set_DOB(self, DOB):
        self.__DOB = DOB

    def get_group_number(self):
        return self.__group_number
    def set_group_number(self, group_number):
        self.__group_number = group_number


jesse = Student("Paul", "27.08.1979", "643", [4, 3, 3, 4, 2])
jesse.display_info()
jesse.set_DOB("24.09.1984")
jesse.set_surname("Pinkman")
jesse.set_group_number("228")
jesse.display_info()