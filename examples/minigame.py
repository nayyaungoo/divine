from src.divine import Heaven, paradise


class MainMenu(Heaven):

    @paradise
    def MainMenu(self):
        """
        Displays the mini-game menu and prompts for a selection.
        
        This method prints the mini-game title and available options—play, load, save, and exit—to the console, then reads the user's input and returns it.
        """
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
        """
        Prints a decorative start message for the 'Itsumi Mario!' game.
        
        Outputs a formatted message indicating the beginning of the game.
        """
        print("--------- ------ ------ Itsumi Mario!")

    @paradise
    def Load(self):
        """
        Prints a message indicating that no files are available to load.
        
        This method notifies the user that there are no saved files present for loading.
        """
        print("--------- ------ ------ No files to load :<")

    @paradise
    def Save(self):
        """
        Prints a confirmation message that the game has been saved.
        
        Outputs a formatted notification to the console confirming that the game state has been saved.
        """
        print("--------- ------ ------ Saved the Game!")

    @paradise
    def Exit(self):
        """
        Prints a farewell message.
        
        Displays a farewell message to signal the user's exit from the game.
        """
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
