import numpy as np

from entity import Entity
from colorama import Fore


class Ball(Entity):
    def __init__(self, position=(10, 10), velocity=(1, 1)) -> None:
        super().__init__(
            name="ball",
            dimens=(1, 1),
            position=position,
            velocity=velocity,
            sprite="O",
            color=Fore.RED,
        )

    def move(self, board) -> None:
        if self.collides(board):
            available = self.available(board)
            W, E, N, S = [int(available[k]) for k in ("W", "E", "N", "S")]
            if W or E:
                self.velocity = self.velocity * np.array([-1, 1])
            if N or S:
                self.velocity = self.velocity * np.array([1, -1])
        self.position += self.velocity
        # implement game over when ball goes below border
