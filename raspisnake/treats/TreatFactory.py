from random import randint

from raspisnake.treats.Apple import Apple
from raspisnake.treats.Blueberry import Blueberry
from raspisnake.treats.Lemon import Lemon
from raspisnake.treats.Orange import Orange
from raspisnake.treats.Plum import Plum
from raspisnake.treats.Strawberry import Strawberry


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

