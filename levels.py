from boss import Boss

from colorama import Fore

from config import *


class Level:
    def __init__(self, layout=[[]], entities=[]) -> None:
        self.layout = layout
        self.entities = entities


LEVEL_1 = Level(
    layout=[
        [(4, None), (3, None), (2, "SP"), (1, None), (1, None), (2, None), (3, None), (4, None)],
        [(3, None), (4, "EP"), (3, None), (2, None), (2, None), (3, None), (4, "SP"), (3, None)],
        [(2, None), (3, None), (4, None), (3, "EP"), (3, None), (4, None), (3, None), (2, None)],
        [(1, None), (2, None), (3, None), (1, None), (0, "EP"), (3, None), (2, None), (1, None)],
        [(1, None), (2, None), (3, None), (0, None), (1, None), (3, None), (2, None), (1, "EP")],
        [(2, "EP"), (3, None), (4, None), (3, None), (3, None), (4, None), (3, None), (2, None)],
        [(3, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (3, None)],
        [(4, None), (3, "EP"), (2, None), (1, "EP"), (1, None), (2, "SP"), (3, None), (4, None)],
    ],
)

LEVEL_2 = Level(
    layout=[
        [(4, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (4, None)],
        [(4, None), (3, None), (3, None), (2, None), (2, None), (3, None), (3, None), (4, None)],
        [(3, None), (3, None), (0, None), (1, None), (1, None), (0, None), (3, None), (3, None)],
        [(2, None), (2, None), (1, None), (1, None), (1, None), (1, None), (2, None), (2, None)],
        [(2, None), (2, None), (1, None), (1, None), (1, None), (1, None), (2, None), (2, None)],
        [(3, None), (3, None), (0, None), (1, None), (1, None), (0, None), (3, None), (3, None)],
        [(4, None), (3, None), (3, None), (2, None), (2, None), (3, None), (3, None), (4, None)],
        [(4, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (4, None)],
    ],
)

LEVEL_3 = Level(
    layout=[
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [(0, None), None, None, (0, None), (0, None), None, None, (0, None)],
    ],
    entities=[
        Boss(
            dimens=(PADDLE_WIDTH - 12, 1),
            position=((SCREEN_WIDTH // 2) - (PADDLE_WIDTH // 2) + 6, 4),
            color=Fore.BLUE,
            restrict_padding=6,
            sprite="▄",
        ),
        Boss(
            dimens=(PADDLE_WIDTH - 8, 1),
            position=((SCREEN_WIDTH // 2) - (PADDLE_WIDTH // 2) + 4, 5),
            color=Fore.BLUE,
            restrict_padding=4,
        ),
        Boss(
            dimens=(PADDLE_WIDTH, 1),
            position=((SCREEN_WIDTH // 2) - (PADDLE_WIDTH // 2), 6),
            color=Fore.GREEN,
        ),
        Boss(
            dimens=(PADDLE_WIDTH - 4, 1),
            position=((SCREEN_WIDTH // 2) - (PADDLE_WIDTH // 2) + 2, 7),
            color=Fore.MAGENTA,
            restrict_padding=2,
            sprite="▀",
        ),
    ],
)

AVAILABLE_LEVELS = [LEVEL_1, LEVEL_2, LEVEL_3]
