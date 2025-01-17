import time, numpy as np

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
                    game.active_powerups.append(self)

            self.position += self.velocity
        except:
            game.unregister(self)

    def activate(self, entity):
        self.expires = time.time() + 4
        entity.dimens *= np.array([1, 1])
        entity.position *= np.array([1, 1])
        entity.velocity *= np.array([1, 1])
        entity.active_powerup = self

    def deactivate(self, entity):
        self.expires = np.inf
        delattr(entity, "active_powerup")


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


class FastBall(Powerup):
    def __init__(self, position, sprite="F") -> None:
        super().__init__(position=position, sprite=sprite)

    def move(self, game) -> None:
        try:
            collision = self.collides(game.board)
            if collision:
                if type(collision).__name__ == "Paddle":
                    balls = list(filter(lambda e: type(e).__name__ == "Ball", game.entities))
                    for ball in balls:
                        self.activate(ball)

            self.position += self.velocity
        except:
            game.unregister(self)

    def activate(self, entity):
        super().activate(entity)
        entity.velocity *= np.array([2, 2])

    def deactivate(self, entity):
        super().deactivate(entity)
        entity.dimens /= np.array([2, 2])
