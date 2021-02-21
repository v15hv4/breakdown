from powerups import ExpandPaddle, FastBall, ShrinkPaddle
import numpy as np

from entity import Entity
from colorama import Fore

colormap = [Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.WHITE]
powermap = {"EP": ExpandPaddle, "SP": ShrinkPaddle, "FB": FastBall}


class Brick(Entity):
    def __init__(self, id, dimens, position, health=4, powerup=None) -> None:
        super().__init__(
            id=id,
            dimens=dimens,
            position=position,
            velocity=(0, 0),
            sprite="⣿",
            color=colormap[health - 1],
        )
        self.health = health
        self.powerup = powermap[powerup](position) if powerup else None

    def hit(self, game) -> None:
        if self.health > 0:
            self.health -= 1
            if self.health > 0:
                self.color = colormap[self.health - 1]

            # break da bricc
            if self.health <= 0:
                game.increment_score()
                game.unregister(self)
                if self.powerup:
                    game.register(self.powerup)
