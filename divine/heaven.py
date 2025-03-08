from curses import newwin
from .realm import Realm


class Heaven(Realm):


    def __init__(self):
        super().__init__()


    def summon(self):
        self.realm = newwin(self.maxy, self.maxx, self.begy, self.begx)
