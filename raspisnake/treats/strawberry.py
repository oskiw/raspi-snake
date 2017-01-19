from raspisnake.color import RED
from raspisnake.treats.treat import Treat


class Strawberry(Treat):

    def __init__(self, position, start_turn):
        super(Strawberry, self).__init__(RED, position, start_turn, 20)

    def on_contact(self, snake):
        snake.crashed = True

    def get_points(self):
        return 0
