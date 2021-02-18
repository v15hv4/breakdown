import numpy as np

from entity import Entity
from colorama import Fore


class Paddle(Entity):
    def __init__(self, dimens=(15, 1), position=(40, 40), velocity=(4, 0)) -> None:
        super().__init__(
            id="paddle",
            dimens=dimens,
            position=position,
            velocity=velocity,
            sprite="▀",
            color=Fore.CYAN,
        )

    def move(self, game) -> None:
        try:
            vx, vy = self.velocity

            if game.pressed == "a":
                for _ in range(vx):
                    if self.position[0] - 1 > 0:
                        self.position -= np.array([1, 0])

            if game.pressed == "d":
                for _ in range(vx):
                    if self.position[0] + 1 <= game.width - 31:
                        self.position += np.array([1, 0])

        except:
            pass
