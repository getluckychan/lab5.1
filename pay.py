from sys import exit, getsizeof
from methods import Methods


class Pay:
    def __init__(self):
        self.__second = 1
        self.__first = 1

    def init_none(self):
        pass

    def set_first(self, first):
        try:
            if first > 0:
                self.__first = first
        except ValueError:
            exit("Введіть додатнє число")

    def set_second(self, second):
        try:
            if second > 0:
                self.__second = second
        except ValueError:
            exit("Введіть додатнє число")

    def get_first(self):
        return self.__first

    def get_second(self):
        return self.__second

    def summa(self):
        return Methods(self.__first) + Methods(self.__second)

    def read(self):
        try:
            self.set_first(float(input("Введіть оклад: ")))
        except BaseException:
            exit("Введіть число")
        try:
            self.set_second(int(input("Введіть відпрацьовані дні:")))
        except BaseException:
            exit("Введіть ціле число")

    def increment_prefix(self):
        x = self.__first
        y = 1
        y += x
        return y

    def decrement_prefix(self):
        x = self.__first
        y = 1
        y -= x
        return y

    def increment_postfix(self):
        x = self.__second
        x += 1
        return x

    def decrement_postfix(self):
        x = self.__second
        x -= 1
        return x

    def to_string(self):
        return str(self.summa()), str(self.increment_prefix()), str(self.decrement_prefix()), str(
            self.increment_postfix()), str(self.decrement_postfix())

    def display(self):
        result = self.to_string()
        return result, getsizeof(Pay)
