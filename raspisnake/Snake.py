from pygame.locals import *
from raspisnake.Coordinates import Coordinates


DEFAULT_SPEED = 0.5


class Snake(object):

    def __init__(self, board):
        self._positions_queue = [Coordinates(3, 3)]
        self._crashed = False
        self._direction = None
        self._board = board
        self._direction_functions = {
            K_DOWN: lambda position: Coordinates(position.x, (position.y + 1) % 8),
            K_UP: lambda position: Coordinates(position.x, (position.y - 1) % 8),
            K_LEFT: lambda position: Coordinates((position.x - 1) % 8, position.y),
            K_RIGHT: lambda position: Coordinates((position.x + 1) % 8, position.y)
        }
        self.reset_attributes()

    def reset_attributes(self):
        self._speed = DEFAULT_SPEED
        self._transform_direction = {
            K_DOWN: K_DOWN,
            K_UP: K_UP,
            K_RIGHT: K_RIGHT,
            K_LEFT: K_LEFT
        }

    @property
    def crashed(self):
        return self._crashed

    @crashed.setter
    def crashed(self, val):
        self._crashed = val

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, val):
        self._speed = val

    @property
    def transform_direction(self):
        return self._transform_direction

    @transform_direction.setter
    def transform_direction(self, val):
        self._transform_direction = val

    def is_moving(self):
        return self._direction is not None

    def update_direction(self, key):
        if len(self._positions_queue) == 1\
                or self.get_next_position_for_key(self._transform_direction.get(key)) != self._positions_queue[-2]:
            self._direction = key

    def is_snake(self, position):
        for p in self._positions_queue:
            if p == position:
                return True
        return False

    def get_next_position(self):
        return self.get_next_position_for_key(self._direction)

    def get_next_position_for_key(self, key):
        return self._direction_functions.get(key)(self.head())

    def remove_tail(self):
        self._board.unset_snake_pixel(self.head())
        self._positions_queue.pop(0)

    def add_head(self, position):
        if self.is_snake(position):
            self._crashed = True
        else:
            self._board.set_snake_pixel(position)
            self._positions_queue.append(position)

    def head(self):
        return self._positions_queue[0]
