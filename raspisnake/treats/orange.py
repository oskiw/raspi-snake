from raspisnake.color import ORANGE
from raspisnake.treats.treat import Treat


class Orange(Treat):

    def __init__(self, position, start_turn):
        super(Orange, self).__init__(ORANGE, position, start_turn, 30)

    def on_contact(self, snake):
        snake.speed = 0.1

    def get_points(self):
        return 3
