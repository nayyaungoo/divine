
__all__ = ['paradise', 'Heaven']

def paradise(func):
    Heaven.paradises.append(func)
    return func


class Heaven(object):
    paradises = []

    def run(self, *args, returnable=False):
        # the list 'received' is always parallel to the list 'paradises'
        self.received = []

        self.paradises = [_ for _ in self.paradises if str(_).startswith(f"<function {self.__class__.__name__}")]

        if len(args) == 0:
            for paradise in self.paradises:
                # Run the all the paradise and store the return value in 'received'
                self.received.append(paradise(self))

        else:
            for index in args:
                # Run the specified Paradises and store the return value in 'received'
                self.received.append(self.paradises[index](self))

        # Strongly recommend to directly use from the list 'received' than returning
        if returnable:
            return self.received
