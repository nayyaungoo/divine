from curses import wrapper, initscr, endwin
from src.divine import *

# input("Method 1 - Procedure")
# -----------------

def procedural():

    menu = Heaven()
    menu.maxy = 10
    menu.maxx = 20
    menu.begy = 0
    menu.begx = 0
    initscr()
    menu.summon()
    menu.border(False)
    menu.write("Helo", 5, 2, pullyx=True)
    menu.write("Helo", 9, 5)
    menu.write("X", pullx=True)
    menu.write("Helo", 1, 1, pullx=True, pully=True)
    menu.write("Helo")
    menu.ask()
    endwin()

procedural()

# input("Method 2 - OOP")
# -----------------

def oop(scr):


    class Menu(Heaven):

        def __init__(self):
            super().__init__()
            self.maxy = 10
            self.maxx = 20
            self.begy = 0
            self.begx = 0

            self.summon()
            self.border()
            self.ask()


    Menu()

# wrapper(oop)
