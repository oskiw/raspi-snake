
class Color(object):

    def __init__(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __neq__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(" + str(self._r) + "," + str(self._g) + "," + str(self._b) + ")"

    def to_list(self):
        return [self._r, self._g, self._b]


WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
BLUE = Color(0, 0, 255)
GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
ORANGE = Color(255, 150, 0)
PURPLE = Color(142, 69, 133)
