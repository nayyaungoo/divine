from curses import window, initscr, endwin
from typing import Optional
from .utilities import classproperty

class StandardScreen:
    __realm: Optional[window] = None
    coordinates: tuple[int, int] = (0, 0)

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
    def dimensions(cls) -> tuple[int, int]:
        return cls.realm.getmaxyx()

def main():
    try:
        from curses import KEY_RESIZE

        StandardScreen.init()
        while True:
            StandardScreen.realm.addstr(f"{StandardScreen.coordinates}")
            StandardScreen.realm.addstr(f"{StandardScreen.dimensions}")

            key = StandardScreen.realm.getch()
            if key != KEY_RESIZE:
                break

            StandardScreen.realm.clear()

    finally:
        StandardScreen.deinit()

if __name__ == '__main__':
    main()
