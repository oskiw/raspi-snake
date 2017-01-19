from sense_hat import SenseHat
from raspisnake.color import *
from time import sleep


class Board(object):

    def __init__(self):
        self._sense = SenseHat()
        self._sense.clear()

    def clear(self):
        self._sense.clear()

    def set_pixel(self, position, color):
        self._sense.set_pixel(position.x, position.y, color.r, color.g, color.b)

    def set_snake_pixel(self, position):
        self.set_pixel(position, WHITE)

    def unset_snake_pixel(self, position):
        self.set_pixel(position, BLACK)

    def show_points(self, points):
        self._sense.clear()
        self._sense.show_message(str(points) + "pts", scroll_speed=0.15,
                                 text_colour=WHITE.to_list(), back_colour=BLACK.to_list())
        sleep(1)
        self._sense.clear()
