from typing import Optional, Any
from curses import window, initscr, endwin

# might be renamed later
class StandardScreen(type):
    __realm: Optional[window] = None

    @classmethod
    def init(cls) -> None:
        cls.__realm = initscr()

    @classmethod
    def deinit(cls) -> None:
        endwin()
        cls.__realm = None

    def __getattribute__(self, name) -> int | Any:

        if name in ('y', 'x', 'height', 'width'):
            if self.__realm is None:
                raise TypeError("The library hasn't been initialized. Try calling `STDSCR.init()`.")

            elif name in ('y', 'x'):
                return 0

            elif name == 'height':
                return self.__realm.getmaxyx()[0]

            elif name == 'width':
                return self.__realm.getmaxyx()[1]

        return super().__getattribute__(name)

class STDSCR(metaclass=StandardScreen):
    y: int
    x: int
    height: int
    width: int

def main():
    STDSCR.init()

    try:
        while True:
            STDSCR._StandardScreen__realm.addstr(f'{STDSCR.y, STDSCR.x}')
            STDSCR._StandardScreen__realm.addstr(f'{STDSCR.height, STDSCR.width}')
            STDSCR._StandardScreen__realm.getch()
            STDSCR._StandardScreen__realm.clear()

    finally:
        STDSCR.deinit()

if __name__ == '__main__':
    main()