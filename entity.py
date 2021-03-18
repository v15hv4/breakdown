import sys, numpy as np

from collections import namedtuple
from colorama import Fore


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
        self.dimens = np.array(dimens)
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.sprite = sprite
        self.color = color

    def collides(self, board) -> bool:
        new_y, new_x = self.position + self.velocity
        if (new_y >= len(board[0])) or (new_y < 0) or (new_x < 0):
            return Entity()
        return board[new_x][new_y]

    def available(self, board) -> dict:
        y, x = self.position
        v_y, v_x = self.velocity
        return {
            "N": (x - abs(v_x) > 0) and (board[x - v_x][y] == None),
            "S": (x + abs(v_x) < len(board)) and (board[x + v_x][y] == None),
            "W": (y - abs(v_y) > 0) and (board[x][y - v_y] == None),
            "E": (y + abs(v_y) < len(board[0])) and (board[x][y + v_y] == None),
        }

    def move(self, game) -> None:
        return
