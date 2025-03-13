from curses import wrapper
from src.divine import *


def main(scr):

    class MainMenu(Heaven):

        def __init__(self):
            super().__init__()

            self.maxy = 13
            self.maxx = 33

            self.summon()
            menu = {
                1 : "Start Game",
                2 : "Save Game",
                3 : "Load Game",
                0 : "Exit Game",
            }
            selected = None

            while True:
                self.clear()
                self.border()

                self.write("Mini Game", 2, 5)
                self.write("=========", leading=1)

                for option, menu_item in menu.items():
                    if selected == option:
                        self.write(f"{option}.{menu_item} [Selected]")
                    elif option == 0:
                        self.write(f"{option}.{menu_item}", leading=1)
                    else:
                        self.write(f"{option}.{menu_item}")

                selected = self.ask("Enter an option: ", type=int)

                if selected == 0:
                    break

    MainMenu()

wrapper(main)

# Using pullx instead of adding y and x are better
# than adding everything because when it is time 
# for you to change the root y and x for whatever 
# reason, you will need to change all the other y 
#  and x after root
#
#                                       - biscuit