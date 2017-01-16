from raspisnake.Color import YELLOW
from raspisnake.treats.Treat import Treat


class Lemon(Treat):

    def __init__(self, position, start_turn):
        super(Lemon, self).__init__(YELLOW, position, start_turn, 10)

    def on_contact(self, snake):
        snake.speed = 1

    def get_points(self):
        return 1
