from src.divine import Heaven, paradise

class Navbar(Heaven):

    @paradise
    def menu(self):
        print("\nNAVIGATION BAR")
        print("==============")
        print(" 0/  Home")
        print(" 1/  About")
        print(" 2/  Pricing")
        print(" 3/  Accounts\n")
        print(" X/  DISCONNECT\n")
        option = input("> Choose an option: ")
        return option


class Accounts(Heaven):

    @paradise
    def menu(self):
        print("\nACCOUNT CENTER")
        print("==============")
        print(" 0/  Login")
        print(" 1/  SignUp\n")
        option = input("> Choose an option: ")
        return option

    username = 'admin'
    password = '12345'

    @paradise
    def login(self):
        print("* Enter your username:")
        username = input("  ")
        print("* Enter your password:")
        password = input("  ")

        return True if (username, password) == (self.username, self.password) else False

    @paradise
    def signup(self):
        print("* Create a new username:")
        username = input("  ")
        print("* Create a new password:")
        password = input("  ")
        self.username = username
        self.password = password

_Navbar = Navbar()
_Accounts = Accounts()

while True:
    _Navbar.run(0)

    if  _Navbar.received[0] == '3':

        _Accounts.run(0)

        match _Accounts.received[0]:
            case '0':
                while True:
                    _Accounts.run(1, returnable=True)

                    if _Accounts.received[0]:
                        print(f"\nWecome back, {_Accounts.username}!")
                        break

                    else:
                        print("\nUsername or Password is incorrect.")

            case '1':
                _Accounts.run(2)

    elif _Navbar.received[0].lower() == 'x':
        break


print(_Navbar.paradises)
print(_Accounts.paradises)