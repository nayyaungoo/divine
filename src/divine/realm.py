import curses
from .layout import Layout
from .cursor import Cursor


class Realm(Layout):

    def __init__(self):
        super().__init__()
        self.realm: curses.window
        self.has_border = False
        self.cursor = Cursor()
        curses.echo()

    @property
    def status(self):
        return hasattr(self, 'realm')

    def border(self, activate=True):
        """
        Parameters
        ----------
        activate: bool, optional
            True: Realm will draw a border around the Heaven
            False: Realm will replace the existed border with ' '

        Raises
        ------
        TypeError
            If Realm have not been summoned
        """

        self.__validate_status()
        if activate:
            self.realm.border()
            self.has_border = True
        else:
            self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
            self.has_border = False

    def ask(self, question='', *coordinates, pully=False, pullx=False, pullyx=False, leading=0, returnable=False):
        self.__validate_status()

        y, x = self.__extract_coordinates(coordinates)
        self.write(question, y, x, pully=pully, pullx=pullx, pullyx=pullyx, leading=leading)

        answer = self.realm.getstr().decode('utf-8')
        
        return answer if not returnable else (answer, question, y, x, returnable)

    def write(self, text, *coordinates, pully=False, pullx=False, pullyx=False, leading=0, returnable=False):
        self.__validate_status()
        y, x = self.__extract_coordinates(coordinates)

        # All these pulls should only affect the next write()
        if pully: self.__pully(y)
        if pullx: self.__pullx(text, x)
        if pullyx: self.__pullyx(text, y, x)

        self.__leading(leading)

        self.realm.addstr(y, x, str(text))
        if returnable: return (text, y, x)

    def refresh(self):
        self.realm.refresh()

    def clear(self):
        self.realm.clear()

    def __validate_status(self):
        if not self.status:
            raise TypeError(f"Realm methods are usable only after summoning. Use summon() to summon one. self.status: {self.status}")

    def __extract_coordinates(self, coordinates):
        if len(coordinates) not in (0, 2):
            raise ValueError(f"The numbers of received coordinates should be either 2 or nothing at all. Received: {len(coordinates)}")

        elif len(coordinates) == 0:
            y = 0 + self.has_border + self.cursor.y
            x = 0 + self.has_border + self.cursor.x
            self.cursor.y += 1
            self.cursor.x = 0

        elif len(coordinates) == 2:
            y = coordinates[0]
            x = coordinates[1]

        return (y, x)

    def __pully(self, y):
        self.cursor.y = y + 1 if not self.has_border else y + 0
        self.cursor.x = 0

    def __pullx(self, text, x):
        self.cursor.x = x - self.has_border

    def __pullyx(self, text, y, x):
        self.cursor.y = y - self.has_border
        self.cursor.x = x + len(text) - self.has_border

    def __leading(self, leading):
        self.cursor.y += leading
