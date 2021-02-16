import os
import signal
import sys
import termios
import time
import tty

from colorama import Fore

from entity import Entity


def getchar():
    # Returns a single character from standard input
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


class Game:
    def __init__(self, framerate=0.03) -> None:
        current_size = os.get_terminal_size()
        self.height = current_size.lines - 1
        self.width = current_size.columns
        self.framerate = framerate
        self.entities = []
        self.board = []
        self.over = False
        self.pressed = None

        # handle game over signal
        signal.signal(signal.SIGUSR1, self.end_game)

        # handle game start signal
        signal.signal(signal.SIGUSR2, self.start_game)

    def start_game(self, *args, **kwargs):
        self.over = True

    def end_game(self, *args, **kwargs):
        self.over = True

    def reset(self) -> None:
        self.board = [[None for _ in range(self.width)] for _ in range(self.height)]

        border_topleft = Entity(sprite="+")
        border_topright = Entity(sprite="+")
        border_horizontal = Entity(sprite="-")
        border_vertical = Entity(sprite="|")

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

    def register(self, entity) -> None:
        self.entities.append(entity)

    def unregister(self, entity) -> None:
        self.entities = list(filter(lambda e: e.id != entity.id, self.entities))

    def end_screen(self) -> None:
        message = "oof."
        print("\n" * (self.height // 2), end="", sep="")
        print(" " * ((self.width // 2) - (len(message) // 2)), end="", sep="")
        print(message)
        print("\n" * (self.height // 2), end="", sep="")

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

    def play(self) -> None:
        while True:
            signal.signal(signal.SIGALRM, lambda *a: 1 / 0)

            try:
                begin = time.monotonic()
                signal.setitimer(signal.ITIMER_REAL, 0.05)
                os.system("clear")

                if self.over:
                    self.end_screen()
                else:
                    self.blit()

                self.pressed = getchar()
                if self.pressed == "x":
                    return

            except:
                self.pressed = None
