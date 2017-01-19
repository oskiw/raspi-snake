from raspisnake.color import YELLOW
from raspisnake.treats.treat import Treat


class Lemon(Treat):

    def __init__(self, position, start_turn):
        super(Lemon, self).__init__(YELLOW, position, start_turn, 10)

    def on_contact(self, snake):
        snake.speed = 0.3

    def get_points(self):
        return 2
