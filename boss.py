from paddle import Paddle

from colorama import Fore


class Boss(Paddle):
    def __init__(
        self,
        id="boss",
        dimens=(15, 1),
        position=(40, 40),
        velocity=(4, 0),
        sprite="█",
        color=Fore.CYAN,
        restrict_padding=0,
    ) -> None:
        super().__init__(
            id=id,
            dimens=dimens,
            position=position,
            velocity=velocity,
            sprite=sprite,
            color=color,
            restrict_padding=restrict_padding,
        )
