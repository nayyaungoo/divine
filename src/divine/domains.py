from typing import Union
from curses import window, initscr, endwin

domain = Union['StandardScreen', 'Hell']

class Hell:
    def __init__(self) -> None:
        self.coordinates = None
        self.dimensions = None

def init():
    global initialized
    initialized = True
    global STDSCR
    STDSCR = StandardScreen()

initialized: bool = False
STDSCR: domain = Hell()

class StandardScreen:

    realm = initscr()
    endwin() if not initialized else ...

    @property
    def coordinates(self) -> tuple[int, int]:
        try: 
            return StandardScreen.realm.getbegyx()
        finally: 
            endwin() if not initialized else ...

    @property
    def dimensions(self) -> tuple[int, int]:
        try: 
            return StandardScreen.realm.getmaxyx()
        finally: 
            endwin() if not initialized else ...

# test func --
def main() -> None:
    print(STDSCR.coordinates)
    print(STDSCR.dimensions)

# test --
if __name__ == '__main__':
    main()
