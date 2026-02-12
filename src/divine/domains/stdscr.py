from curses import window, initscr, endwin
from ..core import initialized

class StandardScreen:

    realm = initscr()

    @property
    def coordinates(self) -> tuple[int, int]:
        return StandardScreen.realm.getbegyx()

    @property
    def dimensions(self) -> tuple[int, int]:
        return StandardScreen.realm.getmaxyx()