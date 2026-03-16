from curses import window, initscr, endwin
from typing import Optional, Any

class StandardScreen(type):
    __realm: Optional[window] = None

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

    def __getattribute__(self, name: str) -> Any:
        if name in ('realm',
                    'y', 'x',
                    'height','width'):

            if StandardScreen.__realm is None:
                raise RuntimeError("The library is not initialized. Try calling STDSCR.init() first.")

            elif name == 'realm':
                return StandardScreen.__realm

            elif name in ('y', 'x'):
                return 0

            elif name == 'height':
                return StandardScreen.__realm.getmaxyx()[0]

            elif name == 'width':
                return StandardScreen.__realm.getmaxyx()[1]

        return super().__getattribute__(name)

class STDSCR(metaclass=StandardScreen):
    y: int
    x: int
    height: int
    width: int
    realm: window

def main():
    try:
        from curses import KEY_RESIZE

        STDSCR.init()
        while True:
            STDSCR.realm.addstr(f"{STDSCR.y, STDSCR.x}")
            STDSCR.realm.addstr(f"{STDSCR.height, STDSCR.width}")

            key = STDSCR.realm.getch()
            if key != KEY_RESIZE:
                break

            STDSCR.realm.clear()

    finally:
        STDSCR.deinit()

if __name__ == '__main__':
    main()
