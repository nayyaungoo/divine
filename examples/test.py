from curses import wrapper
from src.divine import *


def main(scr):
    class MainMenu(Heaven):
        def __init__(self):
            super().__init__()

            self.maxy = 13
            self.maxx = 30

            self.summon()
            option = ''

            while True:
                self.clear()
                self.border()

                self.write(f"Selected: {option}", 0, 2)

                self.write("Mini Game", 2, 5)
                self.write("=========", leading=1)

                self.write("1.Start Game")
                self.write("2.Save Game")
                self.write("3.Load Game")
                self.write("0.Quit Game", leading=1)

                option = self.ask("Enter an option: ")

                if option not in ('0', '1', '2', '3'):
                    option = ''

                elif option == '0':
                    break

    MainMenu()

wrapper(main)