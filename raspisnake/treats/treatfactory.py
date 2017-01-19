from random import randint

from raspisnake.treats.apple import Apple
from raspisnake.treats.blueberry import Blueberry
from raspisnake.treats.lemon import Lemon
from raspisnake.treats.orange import Orange
from raspisnake.treats.plum import Plum
from raspisnake.treats.strawberry import Strawberry


class TreatFactory(object):

    @staticmethod
    def get_treat(position, turn):
        switcher = {
            0: Blueberry(position, turn),
            1: Lemon(position, turn),
            2: Orange(position, turn),
            3: Plum(position, turn),
            4: Strawberry(position, turn)
        }
        return switcher.get(randint(0, 4), Apple(position, turn))

