from . import types as Type
from .domains.hell import Hell

initialized: bool = False
STDSCR: Type.domain = Hell()

def init():
    global initialized
    initialized = True

    from .domains.stdscr import StandardScreen
    global STDSCR
    STDSCR = StandardScreen()

def deinit():
    global initialized
    initialized = False

    global STDSCR
    STDSCR = Hell()

    from curses import endwin
    endwin()

# test func --
def main() -> None:
    # it works somehow
    init()
    print(STDSCR.coordinates)
    print(STDSCR.dimensions)
    deinit()

# test --
if __name__ == '__main__':
    main()
