import time
import numpy as np

from entity import Entity


class Powerup(Entity):
    def __init__(self, position=(30, 30), sprite="X") -> None:
        super().__init__(
            id="powerup", dimens=(1, 1), position=position, velocity=(0, 1), sprite=sprite
        )
        self.expires = np.inf

    def move(self, game) -> None:
        try:
            collision = self.collides(game.board)
            if collision:
                if type(collision).__name__ == "Paddle":
                    self.activate(collision)

            self.position += self.velocity
        except:
            game.unregister(self)

    def activate(self, entity):
        entity.dimens *= np.array([1, 1])
        entity.position *= np.array([1, 1])
        entity.velocity *= np.array([1, 1])
        self.expires = time.time() + 5

    def deactivate(self, entity):
        entity.dimens /= np.array([1, 1])
        entity.position /= np.array([1, 1])
        entity.velocity /= np.array([1, 1])
        self.expires = np.inf


class ExpandPaddle(Powerup):
    def __init__(self, position, sprite="E") -> None:
        super().__init__(position=position, sprite=sprite)

    def activate(self, entity):
        super().activate(entity)
        entity.dimens += np.array([4, 0])

    def deactivate(self, entity):
        super().deactivate(entity)
        entity.dimens -= np.array([4, 0])


class ShrinkPaddle(Powerup):
    def __init__(self, position, sprite="S") -> None:
        super().__init__(position=position, sprite=sprite)

    def activate(self, entity):
        super().activate(entity)
        entity.dimens -= np.array([4, 0])

    def deactivate(self, entity):
        super().deactivate(entity)
        entity.dimens += np.array([4, 0])
