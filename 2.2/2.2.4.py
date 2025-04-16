class Counter:
    def __init__(self, value=0):
        self.__value = value

    def increase(self):
        self.__value += 1

    def decrease(self):
        self.__value -= 1

    def get_counter_value(self):
        return self.__value


counter = Counter(5)
print(counter.get_counter_value())
counter.increase()
print(counter.get_counter_value())

counter1 = Counter()
counter1.decrease()
counter1.decrease()
print(counter1.get_counter_value())
