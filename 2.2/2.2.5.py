class Some:
    def __init__(self, value_1=5, value_2=10):
        self.__value_1 = value_1
        self.__value_2 = value_2

    def __del__(self):
        print("object deleted")


some = Some()
some1 = Some(1, 7)
