# test file

# NOTE -- works
def main_1():
    from . import core

    core.init()
    print(core.STDSCR.coordinates)
    print(core.STDSCR.dimensions)
    core.deinit()

# NOTE -- still dosen't works - BUT WHYY
def main_2():
    from .core import init, STDSCR, deinit

    init()
    print(STDSCR.coordinates)
    print(STDSCR.dimensions)
    deinit()


if __name__ == '__main__':
    main_1()
    # main_2()
