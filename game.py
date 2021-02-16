import os
import sys
import time
import signal

from entity import Entity
from colorama import Fore


class Game:
    def __init__(self, framerate=0.03) -> None:
        current_size = os.get_terminal_size()
        self.height = current_size.lines - 1
        self.width = current_size.columns
        self.framerate = framerate
        self.entities = []
        self.board = []
        self.over = False

        # handle game over signal
        signal.signal(signal.SIGUSR1, self.end_game)

        # handle game start signal
        signal.signal(signal.SIGUSR2, self.start_game)

    def start_game(self, signum, frame):
        self.over = True

    def end_game(self, signum, frame):
        self.over = True

    def reset(self) -> None:
        self.board = [[*[None] * self.width] for _ in range(self.height)]

        border_topleft = Entity(sprite="+")
        border_topright = Entity(sprite="+")
        border_horizontal = Entity(sprite="-")
        border_vertical = Entity(sprite="|")
        # border_bottomleft = Entity(sprite=" ")
        # border_bottomright = Entity(sprite=" ")

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
                # if i == self.height - 1:
                #     if j == 0:
                #         self.board[i][j] = border_bottomleft
                #     elif j == self.width - 1:
                #         self.board[i][j] = border_bottomright
                #     else:
                #         self.board[i][j] = border_horizontal

    def register(self, entity) -> None:
        self.entities.append(entity)

    def unregister(self, entity) -> None:
        self.entities = list(filter(lambda e: e.id != entity.id, self.entities))

    def blit(self) -> None:
        # update game state
        self.reset()
        for entity in self.entities:
            y, x = entity.position
            entity.move(self)
            for h in range(entity.dimens.h):
                for w in range(entity.dimens.w):
                    self.board[x + h][y + w] = entity

        # render current game state
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    print(
                        f"{self.board[i][j].color}{self.board[i][j].sprite}{Fore.RESET}",
                        sep="",
                        end="",
                    )
                else:
                    print(" ", sep="", end="")
            print()

    def end_screen(self) -> None:
        print("game over.")

    def play(self) -> None:
        while True:
            begin = time.monotonic()
            os.system("clear")

            if self.over:
                self.end_screen()
            else:
                self.blit()

            # delay
            while time.monotonic() - begin < self.framerate:
                pass
