import numpy as np

from entity import Entity
from colorama import Fore


class Brick(Entity):
    def __init__(self, id, dimens, position, color=Fore.WHITE, health=4) -> None:
        super().__init__(
            id=id,
            dimens=dimens,
            position=position,
            velocity=(0, 0),
            sprite=str(health),
            color=color,
        )
        self.health = health

    def hit(self, game):
        self.health -= 1
        self.sprite = str(self.health)

        # break da bricc
        if self.health <= 0:
            game.unregister(self)
