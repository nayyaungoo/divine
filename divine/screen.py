from curses import window, initscr, endwin
from typing import Optional, Literal
from .utilities import classproperty

class StandardScreen:
    __realm: Optional[window] = None
    y: Literal[0] = 0
    x: Literal[0] = 0

    @classmethod
    def init(cls) -> None:
        if cls.__realm is not None:
            raise RuntimeError("The library is already initialized. Cannot be initialized again.")
        cls.__realm = initscr()

    @classmethod
    def deinit(cls) -> None:
        if cls.__realm is None:
            raise RuntimeError("The library is not initialized. Cannot be deinitialized.")
        endwin()
        cls.__realm = None

    @classproperty
    def realm(cls) -> window:
        if cls.__realm is None:
            raise RuntimeError("The library is not initialized. Try calling STDSCR.init() first.")
        return cls.__realm

    @classproperty
    def height(cls) -> int:
        return cls.realm.getmaxyx()[0]

    @classproperty
    def width(cls) -> int:
        return cls.realm.getmaxyx()[1]

def main():
    try:
        from curses import KEY_RESIZE

        StandardScreen.init()
        while True:
            StandardScreen.realm.addstr(f"{StandardScreen.y, StandardScreen.x}")
            StandardScreen.realm.addstr(f"{StandardScreen.height, StandardScreen.width}")

            key = StandardScreen.realm.getch()
            if key != KEY_RESIZE:
                break

            StandardScreen.realm.clear()

    finally:
        StandardScreen.deinit()

if __name__ == '__main__':
    main()
