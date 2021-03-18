import signal
import numpy as np

from entity import Entity
from colorama import Fore

from config import BALL_POSITION, BALL_VELOCITY


class Ball(Entity):
    def __init__(self) -> None:
        super().__init__(
            id="ball",
            dimens=(1, 1),
            position=(20, 20),
            velocity=(0, 0),
            sprite="⬤",
            color=Fore.LIGHTWHITE_EX,
        )

    def reset(self) -> None:
        self.position = np.array(BALL_POSITION)
        self.velocity = np.array([0, 0])

    def start(self) -> None:
        self.velocity = np.array(BALL_VELOCITY)

    def move(self, game) -> None:
        try:
            collision = self.collides(game.board)
            if collision:

                # if collided with a brick, hit it
                if type(collision).__name__ == "Brick":
                    collision.hit(game)

                if type(collision).__name__ == "Paddle":
                    delta = collision.dimens[0] / 5

                    if 0 <= self.position[0] - collision.position[0] < delta:
                        self.velocity = np.array([-3, -1])
                    elif (delta) <= self.position[0] - collision.position[0] < (2 * delta):
                        self.velocity = np.array([-2, -1])
                    elif (3 * delta) <= self.position[0] - collision.position[0] < (4 * delta):
                        self.velocity = np.array([2, -1])
                    elif (4 * delta) <= self.position[0] - collision.position[0] < (5 * delta):
                        self.velocity = np.array([3, -1])
                    else:
                        self.velocity *= np.array([1, -1])

                else:
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
