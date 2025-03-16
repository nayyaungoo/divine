from src.divine import Heaven, paradise


class MainMenu(Heaven):

    @paradise
    def MainMenu(self):
        print("Mini-Game!")
        print("==========")
        print("1.Play Game")
        print("2.Load Game")
        print("3.Save Game")
        print("0.Exit Game")
        option = input(" > Enter an option: ")

        return option

    @paradise
    def Play(self):
        print("--------- ------ ------ Itsumi Mario!")

    @paradise
    def Load(self):
        print("--------- ------ ------ No files to load :<")

    @paradise
    def Save(self):
        print("--------- ------ ------ Saved the Game!")

    @paradise
    def Exit(self):
        print("--------- ------ ------ Bye!")

while True:
    received = MainMenu().run(0, returnable=True)

    if received[0] == '1':
        index = 1

    elif received[0] == '2':
        index = 2

    elif received[0] == '3':
        index = 3

    elif received[0] == '0':
        break

    MainMenu().run(index)
