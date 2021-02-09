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
