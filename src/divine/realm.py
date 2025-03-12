import curses
from .layout import Layout


class Realm(Layout):

    def __init__(self):
        super().__init__()
        self.realm: curses.window

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
        self.realm.border() if activate else self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

    def ask(self):
        self.realm.getch()

    def __validate_status(self):
        if not self.status:
            raise TypeError(f"Realm methods are usable only after summoning. Use summon() to summon one. self.status: {self.status}")
