# test file

# NOTE -- works
def main_1():
    from . import domains

    domains.init()
    print(domains.STDSCR.coordinates)
    print(domains.STDSCR.dimensions)

# NOTE -- dosen't works - WHYY
def main_2():
    from .domains import init, STDSCR

    init()
    print(STDSCR.coordinates)
    print(STDSCR.dimensions)


if __name__ == '__main__':
    main_1()
    # main_2()
