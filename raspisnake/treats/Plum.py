from raspisnake.Color import PURPLE
from raspisnake.treats.Treat import Treat
from raspisnake.Position import Position


class Plum(Treat):

    def __init__(self, position, start_turn):
        super(Plum, self).__init__(PURPLE, position, start_turn, 10)

    def on_contact(self, snake):
        snake.direction_functions = {
            K_DOWN: lambda position: Position(position.x, (position.y - 1) % 8),
            K_UP: lambda position: Position(position.x, (position.y + 1) % 8),
            K_LEFT: lambda position: Position((position.x - 1) % 8, position.y),
            K_RIGHT: lambda position: Position((position.x + 1) % 8, position.y)
        }

    def get_points(self):
        return 3
