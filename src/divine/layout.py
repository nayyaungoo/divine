
class Empty(object):

    def __add__(self, value):
        return Layout().validate(value)

    def __radd__(self, value):
        return Layout().validate(value)


class Value(int):

    @property
    def half(self):
        return self // 2


class Layout(object):

    def __init__(self):
        self.__maxy = Empty()
        self.__maxx = Empty()
        self.__begy = Empty()
        self.__begx = Empty()


    @property
    def maxy(self):
        return self.__maxy

    @property
    def maxx(self):
        return self.__maxx

    @property
    def begy(self):
        return self.__begy

    @property
    def begx(self):
        return self.__begx


    @maxy.setter
    def maxy(self, value):
        self.__maxy = self.validate(value)

    @maxx.setter
    def maxx(self, value):
        self.__maxx = self.validate(value)

    @begy.setter
    def begy(self, value):
        self.__begy = self.validate(value)

    @begx.setter
    def begx(self, value):
        self.__begx = self.validate(value)


    @property
    def has_maxyx(self):
        return Empty not in (type(self.maxy), type(self.maxx))

    @property
    def has_begyx(self):
        return Empty not in (type(self.begy), type(self.begx))

    @property
    def has_allyx(self):
        return self.has_maxyx and self.has_begyx


    @staticmethod
    def validate(value: int | Value | None | Empty):
        """
        Parameters
        ----------
        value: int, Value, None, Empty
            The value you want to validate

        Raises
        ------
        TypeError
            If received value is neither int, Value, None, Empty
        """

        if type(value) not in (int, Value, type(None), Empty):
            raise TypeError(f"Invalid Value. Received: '{type(value).__name__}'. Accept: 'int', 'Value', 'NoneType', 'Empty'")

        elif isinstance(value, int):
            value = Value(value)

        elif isinstance(value, type(None)):
            value = Empty()

        return value
