import numpy as np

from collections import namedtuple
from colorama import Fore

import sys


class Entity:
    def __init__(
        self, dimens=(1, 1), position=(1, 1), velocity=(1, 1), sprite="*", color=Fore.WHITE
    ) -> None:
        self.dimens = namedtuple("dimens", "w h")(*dimens)
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.sprite = color + sprite

    def collides(self, board) -> bool:
        new_x, new_y = self.position + self.velocity
        return board[new_x][new_y] != " "

    def available(self, board) -> dict:
        x, y = self.position
        v_x, v_y = self.velocity
        return {
            "left": board[x - v_x][y] != " ",
            "right": board[x + v_x][y] != " ",
            "up": board[x][y - v_y] != " ",
            "down": board[x][y + v_y] != " ",
        }

    def move(self, board) -> None:
        if self.collides(board):
            available = self.available(board)
            left, right, up, down = [int(available[k]) for k in ("left", "right", "up", "down")]
            self.velocity = self.velocity * np.array([-(left | right) or 1, -(up | down) or 1])
        self.position += self.velocity

