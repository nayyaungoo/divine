from .realm import Realm
from .heaven import Heaven


class Paradise(Realm):


    def __init__(self, parent: Heaven):
        super().__init__()
        self.parent = parent


    def summon(self):
        self.realm = self.parent.realm.subpad(
            self.maxy, 
            self.maxx, 
            self.begy + self.parent.begy, 
            self.begx + self.parent.begx,
        )
