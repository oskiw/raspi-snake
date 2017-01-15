
class Color(object):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getr(self):
        return self.r

    def getg(self):
        return self.g

    def getb(self):
        return self.b

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __neq__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(" + str(self.r) + "," + str(self.g) + "," + str(self.b) + ")"

    def to_list(self):
        return [self.r, self.g, self.b]


WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
BLUE = Color(0, 0, 255)
GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
ORANGE = Color(255, 150, 0)
PURPLE = Color(142, 69, 133)
