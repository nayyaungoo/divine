
class Empty(object):


    def __str__(self):
        return str(type(self).__name__)


    def __add__(self, value):
        return validate_value(value)


    def __radd__(self, value):
        return validate_value(value)


class Value(int):
    ...


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
        self.__maxy = validate_value(value)

    @maxx.setter
    def maxx(self, value):
        self.__maxx = validate_value(value)

    @begy.setter
    def begy(self, value):
        self.__begy = validate_value(value)

    @begx.setter
    def begx(self, value):
        self.__begx = validate_value(value)


    def __str__(self):
        return f'[{self.maxy}, {self.maxx}, {self.begy}, {self.begx}]'


def validate_value(value):
    # Covert the received value to Value() if received value was an 'int'
    if isinstance(value, int):
        value = Value(value)

    # Covert the received value to Empty() if received value was a 'None'
    elif value == None:
        value = Empty()

    # Raise Error if the value is neither Empty() nor Value()
    if type(value) not in (Empty, Value):
        raise ValueError(f"Required: 'int', 'Value()', 'None', 'Empty()'. Received: '{type(value).__name__}'")

    # Else return the value whether it was converted or not
    return value
