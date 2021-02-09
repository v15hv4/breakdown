import os
import sys
import time

from entity import Entity


class Surface:
    def __init__(self, framerate=0.03, borders=False) -> None:
        current_size = os.get_terminal_size()
        self.height = current_size.lines - 1
        self.width = current_size.columns
        self.framerate = framerate
        self.borders = borders
        self.entities = []
        self.board = []
        self.over = False

    def reset(self) -> None:
        self.board = [[*[None] * self.width] for _ in range(self.height)]

        # border = Entity(sprite=" ")

        border_topleft = Entity(sprite="+")
        border_topright = Entity(sprite="+")
        border_horizontal = Entity(sprite="-")
        border_vertical = Entity(sprite="|")
        border_bottomleft = Entity(sprite="+")
        border_bottomright = Entity(sprite="+")

        # draw borders
        for i in range(self.height):
            for j in range(self.width):
                # sides
                if j in [0, self.width - 1]:
                    self.board[i][j] = border_vertical

                # top
                if i == 0:
                    if j == 0:
                        self.board[i][j] = border_topleft
                    elif j == self.width - 1:
                        self.board[i][j] = border_topright
                    else:
                        self.board[i][j] = border_horizontal

                # bottom
                if i == self.height - 1:
                    if j == 0:
                        self.board[i][j] = border_bottomleft
                    elif j == self.width - 1:
                        self.board[i][j] = border_bottomright
                    else:
                        self.board[i][j] = border_horizontal

    def register(self, entity) -> None:
        self.entities.append(entity)

    def blit(self) -> None:
        while True:
            begin = time.monotonic()
            os.system("clear")

            # update game state
            self.reset()
            for entity in self.entities:
                y, x = entity.position
                self.over = entity.move(self.board)
                if not self.over:
                    for h in range(entity.dimens.h):
                        for w in range(entity.dimens.w):
                            self.board[x + h][y + w] = entity
                else:
                    print("game over")
                    return

            # render current game state
            for i in range(self.height):
                for j in range(self.width):
                    if self.board[i][j]:
                        print(self.board[i][j].sprite, sep="", end="")
                    else:
                        print(" ", sep="", end="")
                print()

            # delay
            while time.monotonic() - begin < self.framerate:
                pass
