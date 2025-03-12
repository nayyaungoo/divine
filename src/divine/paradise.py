from .realm import Realm
from .heaven import Heaven


class Paradise(Realm):

    def __init__(self, parent: Heaven):
        super().__init__()
        self.parent = parent

    def summon(self):

        if not self.has_begyx:
            raise TypeError(f"Need layout values begy and begx to summon a Paradise. self.has_begyx: {self.has_begyx}")

        elif not self.has_allyx:
            self.realm = self.parent.realm.subpad(self.begy, self.begx)

        elif self.has_allyx:
            self.realm = self.parent.realm.subpad(self.maxy, self.maxx, self.begy, self.begx)

class Inside(Paradise):

    def __init__(self, parent):
        super().__init__(parent)
        self.maxy = parent.maxy - (1 + self.parent.has_border)
        self.maxx = parent.maxx - (1 + self.parent.has_border)
        self.begy = 0 + self.parent.has_border
        self.begx = 0 + self.parent.has_border