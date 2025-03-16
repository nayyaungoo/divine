
class Realm(type):

    # TODO: Idk why did I even created this :<
    def __new__(cls, clsname, bases, attrs):
        return super().__new__(cls, clsname, bases, attrs)


paradises = []
def paradise(func):
    paradises.append(func)
    return func

class Heaven(metaclass=Realm):

    def run(self, *args, returnable=False):
        self.received = []
        if len(args) == 0:
            for _ in paradises:
                self.received.append(_(self))

        else:
            for index in args:
                self.received.append(paradises[index](self))
        if returnable:
            return self.received
