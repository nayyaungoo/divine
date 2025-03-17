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

row_A = MainMenu()
index = 0

while True:
    row_A.run(index)

    match row_A.received[0]:

        case '1': index = 1
        case '2': index = 2
        case '3': index = 3
        case '0': break
        case _  : index = 0
