from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domains.hell import Hell
    from .domains.stdscr import StandardScreen

domain = Union['StandardScreen', 'Hell']
