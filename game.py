import os
import signal
import sys
import termios
import time
import tty

from colorama import Fore, Back

from entity import Entity


def getchar():
    # return a single character from standard input
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


class TimeoutException(Exception):
    pass


def timeoutException(*args):
    raise TimeoutException


class Game:
    def __init__(self, framerate=60) -> None:
        current_size = os.get_terminal_size()
        self.height = current_size.lines
        self.width = current_size.columns + 1
        self.framerate = framerate
        self.entities = []
        self.board = []
        self.over = False
        self.pressed = None

        self.cursor = {
            "RESET": lambda: f"\x1b[H",
            "DOWN": lambda n: f"\x1b[{n}B",
            "RIGHT": lambda n: f"\x1b[{n}C",
        }

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

        border_topleft = Entity(sprite="┌")
        border_topright = Entity(sprite="┐")
        border_horizontal = Entity(sprite="─")
        border_vertical = Entity(sprite="│")

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

    def blit_gameover(self) -> None:
        os.system("clear")
        message = f"""
{" " * ((self.width // 2) - 10)}⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⣿⣿⣿⠦⠀⠸⣿⣿⡄⢻
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢻⠇⣼
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⠀⠀noob⠀ ⡟⣰
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣼⢀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿
{" " * ((self.width // 2) - 10)}⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸
{" " * ((self.width // 2) - 10)}⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸
        """

        sys.stdout.write("\n" * (self.height // 3))
        sys.stdout.write(" " * ((self.width // 2) - (len(message) // 2)))
        sys.stdout.write(message)
        sys.stdout.flush()
        sys.stdout.write(self.cursor["RESET"]())

        # exit game
        if self.pressed == "\x1b":
            signal.raise_signal(2)

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
                sys.stdout.write(self.cursor["RESET"]())
                sys.stdout.write(f"{self.cursor['DOWN'](i - 1)}{self.cursor['RIGHT'](j - 1)}")
                if self.board[i][j]:
                    sys.stdout.write(
                        f"{self.board[i][j].color}{self.board[i][j].sprite}{Fore.RESET}"
                    )
                else:
                    sys.stdout.write(" ")
            sys.stdout.flush()
        sys.stdout.write(self.cursor["RESET"]())

    def play(self) -> None:
        interval = 1 / self.framerate
        os.system("clear")
        last_pressed = 0
        while True:
            try:
                signal.setitimer(signal.ITIMER_REAL, interval)
                signal.signal(signal.SIGALRM, timeoutException)
                if self.over:
                    self.blit_gameover()
                else:
                    self.blit()
                self.pressed = getchar()
                last_pressed = time.time_ns()
            except TimeoutException:
                self.pressed = None
