from raspisnake.Color import GREEN
from raspisnake.treats.Treat import Treat


class Apple(Treat):

    def __init__(self, position, start_turn):
        super(Apple, self).__init__(GREEN, position, start_turn, 30)

    def on_contact(self, snake):
        return

    def get_points(self):
        return 1
