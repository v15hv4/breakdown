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

        border = Entity(sprite=" ")

        # draw borders
        for i in range(self.height):
            for j in range(self.width):
                # sides
                if j in [0, self.width - 1]:
                    self.board[i][j] = border

                # top
                if i == 0:
                    if j == 0:
                        self.board[i][j] = border
                    elif j == self.width - 1:
                        self.board[i][j] = border
                    else:
                        self.board[i][j] = border

                # bottom
                if i == self.height - 1:
                    if j == 0:
                        self.board[i][j] = border
                    elif j == self.width - 1:
                        self.board[i][j] = border
                    else:
                        self.board[i][j] = border

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
