import numpy as np

from collections import namedtuple
from colorama import Fore

import sys


class Entity:
    def __init__(
        self,
        id="npc",
        dimens=(1, 1),
        position=(1, 1),
        velocity=(0, 0),
        sprite="*",
        color=Fore.WHITE,
    ) -> None:
        self.id = id
        self.dimens = namedtuple("dimens", "w h")(*dimens)
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.sprite = sprite
        self.color = color

    def collides(self, board) -> bool:
        new_y, new_x = self.position + self.velocity
        return board[new_x][new_y]

    def available(self, board) -> dict:
        y, x = self.position
        v_y, v_x = self.velocity
        return {
            "N": board[x - v_x][y] != None,
            "S": board[x + v_x][y] != None,
            "W": board[x][y - v_y] != None,
            "E": board[x][y + v_y] != None,
        }

    def move(self, board) -> None:
        if self.collides(board):
            available = self.available(board)
            W, E, N, S = [int(available[k]) for k in ("W", "E", "N", "S")]
            if W or E:
                self.velocity = self.velocity * np.array([-1, 1])
            if N or S:
                self.velocity = self.velocity * np.array([1, -1])
        self.position += self.velocity
