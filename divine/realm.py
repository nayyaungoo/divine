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

    @x.setter
    def x(self, value):
        self._x = value


class Realm(Layout):


    def __init__(self):
        super().__init__()
        self.has_border = False
        self.realm: curses.window
        self.cursor = Cursor()
        curses.echo(True)


    def border(self, enable=True):

        if enable and not self.has_border:
            self.realm.border()
            self.has_border = True

        elif not enable and self.has_border:
            self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',)
            self.has_border = False


    def write(self, *args, pully=True, pullx=False):

        y, x, text = self.__validate_args(args, pully, pullx)
        self.realm.addstr(y, x, text)


    def ask(self, *args, pully=True, pullx=False, request='str'):
        if len(args) != 0:
            y, x, text = self.__validate_args(args, pully, pullx)
            self.write(text, y, x, pully=pully, pullx=pullx)

        match request:
            case 'str': return self.realm.getstr()
            case 'ch': return self.realm.getkey()


    def __validate_args(self, args, pully, pullx):

        if len(args) == 0:
            raise ValueError(f"Require at least: 1 argument, Receieved: {len(args)}")


        # Tracked Writing
        elif len(args) == 1:

            text = str(args[0])

            if not self.has_border:
                y = 0 + self.cursor.y
                x = 0 + self.cursor.x

            elif self.has_border:
                y = 1 + self.cursor.y
                x = 1 + self.cursor.x

            if not pullx:
                self.cursor.x = 0

            # Even pully is False, it shouldn't affect on a 'Tracked Writing'
            pully = True


        # Scripted Writing
        elif len(args) == 3:

            text = str(args[0])

            y = int(args[1])
            x = int(args[2])


        # Flags

        if pully:
            self.cursor.y += 1

        if pullx:

            if not self.has_border:
                self.cursor.x = x + len(text)
                self.cursor.y = y

            elif self.has_border:
                self.cursor.x = x + len(text) - 1
                self.cursor.y = y - 1


        return (y, x, text)

def wrapper(screen):

    def _(scr):
        screen()

    curses.wrapper(_)