
class Coordinates(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __neq__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(" + str(self._x) + "," + str(self._y) + ")"
