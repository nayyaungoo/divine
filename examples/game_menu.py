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
                0 : "Start Game",
                1 : "Save Game",
                2 : "Load Game",
                3 : "Exit Game",
            }
            selected = 0

            while True:
                self.clear()
                self.border()

                self.write("Mini Game", 2, 5)
                self.write("=========", leading=1)

                for option, menu_item in menu.items():
                    if selected == option:
                        self.write(f"{menu_item} [Selected]")
                    elif option == 0:
                        self.write(f"{menu_item}")
                    else:
                        self.write(f"{menu_item}")

                self.write('')
                option = self.ask("Arrow UP/DOWN to select", type='key')

                if option == 259 and selected > 0:
                    selected -= 1
                elif option == 258 and selected < 3:
                    selected += 1

    MainMenu()

wrapper(main)

# Using pullx instead of adding y and x are better
# than adding everything because when it is time 
# for you to change the root y and x for whatever 
# reason, you will need to change all the other y 
#  and x after root
#
#                                       - biscuit