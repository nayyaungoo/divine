import curses
from .layout import Layout
from .cursor import Cursor


class InsufficientLayout(Exception):
    """ Raised when the realm is being summoned are being called under suffocating """

class RealmNotFound(Exception):
    """ Raised when realm methods are being called without summoning first """


class Realm(Layout):

    def __init__(self):
        super().__init__()
        self.realm: curses.window
        self.has_border = False
        self.cursor = Cursor()
        curses.echo()


    # I'm sorry
    def RealmMethod(func):
        def wrapper(self, *args, **kwargs):
            if not self.status:
                raise RealmNotFound(f"Realm methods are usable only after  summoning. Use summon() to summon one. self.status: {self.status}") 

            return func(self, *args, **kwargs)

        return wrapper


    @property
    def status(self) -> bool:
        """ Returns True if realm has been summoned, otherwise False """

        return hasattr(self, 'realm')


    @RealmMethod
    def border(self, activate=True) -> None:
        """ Draw a border at the edges of the self.realm

        Parameters:
            activate: bool, optional
                True: Realm will draw a border around the Heaven
                False: Realm will replace the existed border with spaces (' ')

        Raises:
            RealmNotFound
                If Realm have not been summoned

        """
        # TODO: Add more parameters for more flexibility and customizability

        if activate:
            self.realm.border()
            self.has_border = True
        else:
            self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
            self.has_border = False


    @RealmMethod
    def ask(self, question='', *coordinates, type='str', pully=True, pullx=True, pullyx=False, leading=0, returnable=False):
        """ Ask user for an input and return it

        Parameters:
            question: str, optional(default: '')
                Received string will be passed to write() and displayed on determined or specified coordinates

            *coordinates: int, int, optional
                Received coordinates will be passed to write() and coordinate the question

                default:
                    y: int = 0 + self.has_border + self.cursor.y
                    x: int = 0 + self.has_border + self.cursor.x

            type: str, optional(default: 'str')
                Determine the return type. Returns 'None' if the type of answer doesn't match 
                the speficifed type, otherwise returns the answer as requested type

            pully: bool, optional(default: True)
                True: The y coordinate of next write() or ask() will follow the current y of ask()
                False: The y coordinate of next write() or ask() will follow the current y of cursor

            pullx: bool, optional(default: True)
                True: The x coordinate of next write() or ask() will follow the current x of ask()
                False: The x coordinate of next write() or ask() will follow the current x of cursor

            pullyx: bool, optional(default: False)
                True: The next write() or ask() will be displayed right after the end of the question
                False: The next write() or ask() will be displayed on determined or specified coordinates

            leading: int, optional(default: 0)
                The y gap between current ask() and next ask() or write()

            returable: bool, optional(default: False)
                True: Returns (answer, question, y, x, returnable)
                False: Returns answer

        Raises:
            RealmNotFound
                If Realm have not been summoned

        """

        y, x = self.__extract_coordinates(coordinates)
        self.write(question, y, x, pully=pully, pullx=pullx, pullyx=pullyx, leading=leading)

        match type:
            case 'str': answer = self.__ask_str()
            case 'int': answer = self.__ask_int()
            case 'key': answer = self.__ask_key()

        return answer if not returnable else (answer, question, y, x)


    @RealmMethod
    def write(self, text='', *coordinates, pully=True, pullx=True, pullyx=False, leading=0, returnable=False):
        """ Display a string

        Parameters:
            text: str, optional(default: '')
                Received string will be displayed on determined or specified coordinates

            *coordinates: int, int, optional
                Received coordinates will coordinate the text

                default:
                    y: int = 0 + self.has_border + self.cursor.y
                    x: int = 0 + self.has_border + self.cursor.x

            pully: bool, optional(default: True)
                True: The y coordinate of next write() or ask() will follow the current y of ask()
                False: The y coordinate of next write() or ask() will follow the current y of cursor

            pullx: bool, optional(default: True)
                True: The x coordinate of next write() or ask() will follow the current x of ask()
                False: The x coordinate of next write() or ask() will follow the current x of cursor

            pullyx: bool, optional(default: False)
                True: The next write() or ask() will be displayed right after the end of the question
                False: The next write() or ask() will be displayed on determined or specified coordinates

            leading: int, optional(default: 0)
                The y gap between current ask() and next ask() or write()

            returable: bool, optional(default: False)
                True: Returns (text, y, x, returnable)
                False: Returns 'None'

        Raises:
            RealmNotFound
                If Realm have not been summoned

        """

        y, x = self.__extract_coordinates(coordinates)

        # All these pulls should only affect the next write()
        if pully: self.__pully(y)
        if pullx: self.__pullx(text, x)
        if pullyx: self.__pullyx(text, y, x)

        self.__leading(leading)

        self.realm.addstr(y, x, str(text))
        if returnable: return (text, y, x)


    def refresh(self):
        # TODO: Make it more useful and add documentation
        self.realm.refresh()


    def clear(self):
        # TODO: Make it more useful and add documentation
        self.realm.clear()


    def __extract_coordinates(self, coordinates):
        if len(coordinates) not in (0, 2):
            raise ValueError(f"The numbers of received coordinates should be either 2 or nothing at all. Received: {len(coordinates)}")

        elif len(coordinates) == 0:
            y = 0 + self.has_border + self.cursor.y
            x = 0 + self.has_border + self.cursor.x
            self.cursor.y += 1
            self.cursor.x = 0

        elif len(coordinates) == 2:
            y = coordinates[0]
            x = coordinates[1]

        return (y, x)

    def __pully(self, y):
        self.cursor.y = y + 1 if not self.has_border else y + 0
        self.cursor.x = 0

    def __pullx(self, text, x):
        self.cursor.x = x - self.has_border

    def __pullyx(self, text, y, x):
        self.cursor.y = y - self.has_border
        self.cursor.x = x + len(text) - self.has_border

    def __leading(self, leading):
        self.cursor.y += leading

    def __ask_str(self):
        return self.realm.getstr().decode('utf-8')

    def __ask_int(self):
        try: return int(self.__ask_str())
        except ValueError: pass

    def __ask_key(self):
        self.realm.keypad(True)
        return self.realm.getch()
