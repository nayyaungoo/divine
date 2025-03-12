import curses
from .realm import Realm


class Heaven(Realm):

    def __init__(self):
        super().__init__()

    def summon(self, endless=False):
        """
        Parameters
        ----------
        endless: bool, optional
            An endless Heaven is not restricted by the screen size, and is not 
            necessarily associated with a particular part of the screen.

        Raises
        ------
        TypeError
            If Heaven have neither maxy nor maxx
        """

        if not self.has_maxyx:
            raise TypeError(f"Need layout values maxy and maxx to summon a Heaven. self.has_maxyx: {self.has_maxyx}")

        elif not self.has_allyx and not endless:
            self.realm = curses.newwin(self.maxy, self.maxx)

        elif self.has_allyx and not endless:
            self.realm = curses.newwin(self.maxy, self.maxx, self.begy, self.begx)

        elif self.has_maxyx and endless:
            self.realm = curses.newpad(self.maxy, self.maxx)
