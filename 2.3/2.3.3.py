class Calculation:
    def __init__(self, calculation_line):
        self.__calculation_line = calculation_line

    def set_last_symbol_calculation_line(self, symbol):
        self.__calculation_line += symbol

    def get_last_symbol(self):
        return self.get_calculation_line()[-1]

    def delete_last_symbol(self):
        self.set_calculation_line(self.get_calculation_line()[:-1])

    def get_calculation_line(self):
        return self.__calculation_line
    def set_calculation_line(self, calculation_line):
        self.__calculation_line = calculation_line


str = Calculation("12345")
print(str.get_calculation_line())
str.delete_last_symbol()
print(str.get_calculation_line())
print(str.get_last_symbol())
str.set_last_symbol_calculation_line("a")
print(str.get_calculation_line())