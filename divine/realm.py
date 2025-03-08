import curses
from .layout import Layout

class Cursor(object):


    def __init__(self):
        self._y = 0
        self._x = 0


    @property
    def y(self):
        return self._y

    @property
    def x(self):
        return self._x


    @y.setter
    def y(self, value):
        self._y = value


class Realm(Layout):


    def __init__(self):
        super().__init__()
        self.has_border = False
        self.realm: curses.window
        self.cursor = Cursor()


    def border(self, enable=True):
        
        if enable and not self.has_border:
            self.realm.border()
            self.has_border = True
        
        elif not enable and self.has_border:
            self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',)
            self.has_border = False


    def write(self, *args):

        y, x, text = self.__validate_args(args)
        self.realm.addstr(y, x, text)


    def ask(self):
        self.realm.getch()


    def __validate_args(self, args):

        if len(args) == 0:
            raise ValueError(f"Require at least: 1 argument, Receieved: {len(args)}")

        elif len(args) == 1:

            text = str(args[0])

            if not self.has_border:
                y = 0 + self.cursor.y
                x = 0 + self.cursor.x

            elif self.has_border:
                y = 1 + self.cursor.y
                x = 1 + self.cursor.x

            self.cursor.y += 1

        elif len(args) == 3:

            text = str(args[0])

            y = int(args[1])
            x = int(args[2])

        return (y, x, text)
