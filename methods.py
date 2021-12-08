class Methods:
    def __init__(self, x):
        self.__x = x

    def __add__(self, other):
        return self.__x / 30 * other.__x

    def __iadd__(self, other):
        self.__x = self + other
        return self.__x

    def __isub__(self, other):
        self.__x = self - other
        return self.__x