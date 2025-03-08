from .layout import Layout

class Realm(Layout):


    def __init__(self):
        super().__init__()
        self.has_border = False


    def border(self, enable=True):
        
        if enable and not self.has_border:
            self.realm.border()
            self.has_border = True
        
        elif not enable and self.has_border:
            self.realm.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',)
            self.has_border = False


    def ask(self):
        self.realm.getch()
