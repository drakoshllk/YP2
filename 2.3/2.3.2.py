class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def get_salary(self):
        print(f'Worker salary: {self.get_rate() * self.get_days()}')

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname
    def set_surname(self, surname):
        self.__surname = surname

    def get_rate(self):
        return self.__rate
    def set_rate(self, rate):
        self.__rate = rate

    def get_days(self):
        return self.__days
    def set_days(self, days):
        self.__days = days