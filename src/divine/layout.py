
class Empty(object):

    def __add__(self, value):
        return Layout().validate(value)

    def __radd__(self, value):
        return Layout().validate(value)


class Value(int):

    @property
    def half(self):
        return self // 2


class Layout(object):

    @staticmethod
    def validate(value: int | Value | None | Empty):
        """
        Parameters
        ----------
        value: int, Value, None, Empty
            The value you want to validate

        Raises
        ------
        TypeError
            If received value is neither int, Value, None, Empty
        """

        if type(value) not in (int, Value, type(None), Empty):
            raise TypeError(f"Invalid Value. Received: '{type(value).__name__}'. Accept: 'int', 'Value', 'NoneType', 'Empty'")

        elif isinstance(value, int):
            value = Value(value)

        elif isinstance(value, type(None)):
            value = Empty()

        return value
