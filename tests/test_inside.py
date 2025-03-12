from curses import wrapper
from src.divine import *


def main(scr):

    class MainMenu(Heaven):

        def __init__(self):
            super().__init__()

            self.maxy = 13
            self.maxx = 30

            self.summon()
            self.border()
            self.refresh()

            class Inside():

                def __init__(self, parent):
                    super().__init__(parent)

                    self.summon()
                    self.ask()

            Inside(self)

    MainMenu()

wrapper(main)