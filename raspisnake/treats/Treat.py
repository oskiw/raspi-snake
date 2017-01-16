
class Treat(object):

    def __init__(self, color, position, start_turn, expiration):
        self._color = color
        self._start_turn = start_turn
        self._expiration = expiration
        self._position = position

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    def has_expired(self, turn):
        return self._start_turn + self._expiration < turn

    def on_contact(self, snake):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_points(self):
        raise NotImplementedError("Subclass must implement abstract method")

