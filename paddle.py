import numpy as np

from colorama import Fore
from entity import Entity


class Paddle(Entity):
    def __init__(
        self,
        id="paddle",
        dimens=(15, 1),
        position=(40, 40),
        velocity=(4, 0),
        color=Fore.CYAN,
        sprite="▀",
        restrict_padding=0,
    ) -> None:
        super().__init__(
            id=id,
            dimens=dimens,
            position=position,
            velocity=velocity,
            sprite=sprite,
            color=color,
        )
        self.restrict_padding = restrict_padding

    def move(self, game) -> None:
        try:
            vx, vy = self.velocity

            if game.pressed == "a":
                for _ in range(vx):
                    if self.position[0] - 1 > self.restrict_padding:
                        self.position -= np.array([1, 0])

            if game.pressed == "d":
                for _ in range(vx):
                    if (self.position[0] + 1 + self.dimens[0] + 1) <= (
                        game.width - self.restrict_padding
                    ):
                        self.position += np.array([1, 0])

        except:
            pass
