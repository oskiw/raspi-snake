from raspisnake.Color import PURPLE
from raspisnake.treats.Treat import Treat


class Plum(Treat):

    def __init__(self, position, start_turn):
        super(Plum, self).__init__(PURPLE, position, start_turn, 10)

    def on_contact(self, snake):
        snake.set_crashed(True)

    def get_points(self):
        return 0
