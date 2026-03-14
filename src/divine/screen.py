# boilerplates. boilerplates everywhere

from typing import Optional
from curses import window, initscr, endwin

class classproperty:
    def __init__(self, func):
        self.fget = func
    def __get__(self, instance, owner):
        return self.fget(owner)

class STDSCR:
    __realm: Optional[window] = None

    @classmethod
    def init(cls) -> None:
        cls.__realm = initscr()

    @classmethod
    def deinit(cls) -> None:
        endwin()
        cls.__realm = None

    @classproperty
    def y(cls) -> int:
        if cls.__realm is None:
            raise TypeError("The standard screen hasn't been initialized.")
        return 0

    @classproperty
    def x(cls) -> int:
        if cls.__realm is None:
            raise TypeError("The standard screen hasn't been initialized.")
        return 0

    @classproperty
    def height(cls) -> int:
        if cls.__realm is None:
            raise TypeError("The standard screen hasn't been initialized.")
        return cls.__realm.getmaxyx()[0]

    @classproperty
    def width(cls) -> int:
        if cls.__realm is None:
            raise TypeError("The standard screen hasn't been initialized.")
        return cls.__realm.getmaxyx()[1]

def main():
    STDSCR.init()

    try:
        while True:
            STDSCR._STDSCR__realm.addstr(f'{STDSCR.y, STDSCR.x}')
            STDSCR._STDSCR__realm.addstr(f'{STDSCR.height, STDSCR.width}')
            STDSCR._STDSCR__realm.getch()
            STDSCR._STDSCR__realm.clear()

    finally:
        STDSCR.deinit()

if __name__ == '__main__':
    main()
