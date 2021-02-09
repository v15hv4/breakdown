import os
import sys
import time


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
        self.board = [[*[" "] * self.width] for _ in range(self.height)]

        # draw borders
        for i in range(self.height):
            for j in range(self.width):
                # sides
                if j in [0, 1, self.width - 1, self.width - 2]:
                    self.board[i][j] = "┃" if self.borders else "⠀"

                # top
                if i == 0:
                    if j == 0:
                        self.board[i][j] = "┏" if self.borders else "⠀"
                    elif j == self.width - 1:
                        self.board[i][j] = "┓" if self.borders else "⠀"
                    else:
                        self.board[i][j] = "━" if self.borders else "⠀"

                # bottom
                if i == self.height - 1:
                    if j == 0:
                        self.board[i][j] = "┗" if self.borders else "⠀"
                    elif j == self.width - 1:
                        self.board[i][j] = "┛" if self.borders else "⠀"
                    else:
                        self.board[i][j] = "━" if self.borders else "⠀"

                    # if i == 10:
                    #     if 5 < j < 50:
                    #         self.board[i][j] = "|"

                    # if i == 30:
                    #     if 30 < j < 80:
                    #         self.board[i][j] = "|"

    def register(self, entity) -> None:
        self.entities.append(entity)

    def blit(self) -> None:
        while True:
            begin = time.monotonic()
            os.system("clear")

            # get current game state
            self.reset()
            for entity in self.entities:
                y, x = entity.position
                self.over = entity.move(self.board)
                if not self.over:
                    for h in range(entity.dimens.h):
                        for w in range(entity.dimens.w):
                            self.board[x + h][y + w] = entity.sprite
                else:
                    print("game over")
                    return

            # render current game state
            for i in range(self.height):
                for j in range(self.width):
                    print(self.board[i][j], sep="", end="")
                print()

            # delay
            while time.monotonic() - begin < self.framerate:
                pass
