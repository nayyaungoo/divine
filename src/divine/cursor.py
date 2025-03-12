
class Cursor(object):
    def __init__(self):
        self._y = 0
        self._x = 0

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value