import numpy as np

from entity import Entity
from colorama import Fore


class Paddle(Entity):
    def __init__(self, dimens=(15, 1), position=(40, 40), velocity=(2, 0)) -> None:
        super().__init__(
            id="paddle",
            dimens=dimens,
            position=position,
            velocity=velocity,
            sprite="M",
            color=Fore.YELLOW,
        )

    def move(self, game) -> None:
        try:
            if game.pressed == "a":
                self.position -= self.velocity
            elif game.pressed == "d":
                self.position += self.velocity
        except:
            pass
