from collections import namedtuple
from colorama import Fore


class Entity:
    def __init__(
        self, dimens=(1, 1), position=(1, 1), velocity=(0, 0), sprite="x", color=Fore.WHITE
    ) -> None:
        self.dimens = namedtuple("dimens", "w h")(*dimens)
        self.position = namedtuple("position", "x y")(*position)
        self.velocity = namedtuple("velocity", "x y")(*velocity)
        self.sprite = color + sprite
