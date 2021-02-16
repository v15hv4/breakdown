import numpy as np

from entity import Entity
from colorama import Fore


class Paddle(Entity):
    def __init__(self, dimens=(7, 1), position=(40, 40)) -> None:
        super().__init__(
            id="paddle", dimens=dimens, position=position, sprite="M", color=Fore.YELLOW
        )

    def move(self, game) -> None:
        try:
            if game.pressed == "a":
                self.position -= np.array([1, 0])
            elif game.pressed == "d":
                self.position += np.array([1, 0])
        except:
            pass
