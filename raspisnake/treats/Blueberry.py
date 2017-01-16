from raspisnake.Color import BLUE
from raspisnake.treats.Treat import Treat


class Blueberry(Treat):

    def __init__(self, position, start_turn):
        super(Blueberry, self).__init__(BLUE, position, start_turn, 30)

    def on_contact(self, snake):
        snake.revertx = True

    def get_points(self):
        return 3
