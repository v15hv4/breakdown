import signal
import numpy as np

from entity import Entity
from colorama import Fore


class Ball(Entity):
    def __init__(self, position=(1, 1), velocity=(1, 1)) -> None:
        super().__init__(
            id="ball",
            dimens=(1, 1),
            position=position,
            velocity=velocity,
            sprite="O",
            color=Fore.RED,
        )

    def move(self, game) -> None:
        try:
            collision = self.collides(game.board)
            if collision:

                # if collided with a brick, hit it
                if type(collision).__name__ == "Brick":
                    collision.hit(game)

                available = self.available(game.board)
                W, E, N, S = [int(available[k]) for k in ("W", "E", "N", "S")]
                if not W or not E:
                    self.velocity *= np.array([-1, 1])
                if not N or not S:
                    self.velocity *= np.array([1, -1])
            self.position += self.velocity

        except:
            # implement game over when ball goes below border
            signal.raise_signal(10)
