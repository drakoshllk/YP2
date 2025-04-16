class Two_numbers:
    def __init__(self, number_1, number_2):
        self.__number_1 = number_1
        self.__number_2 = number_2

    def display_numbers(self):
        print(f'first number: {self.get_number_1()}\n'
              f'second number: {self.get_number_2()}')

    def sum(self):
        return self.get_number_1() + self.get_number_2()

    def greatest(self):
        return max(self.get_number_1(), self.get_number_2())

    def get_number_1(self):
        return self.__number_1
    def set_number_1(self, number_1):
        self.__number_1 = number_1

    def get_number_2(self):
        return self.__number_2
    def set_number_2(self, number_2):
        self.__number_2 = number_2


num = Two_numbers(5, 10)
num.display_numbers()
print(f'sum: {num.sum()}\n'
      f'greatest: {num.greatest()}\n')

num.set_number_1(20)
num.set_number_2(30)
num.display_numbers()
print(f'sum: {num.sum()}\n'
      f'greatest: {num.greatest()}\n')