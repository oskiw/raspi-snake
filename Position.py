
class Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __neq__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
