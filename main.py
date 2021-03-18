import os
import signal

from random import randint
from sys import stdout

from colorama import Fore, init, deinit

from config import SCREEN_HEIGHT, SCREEN_WIDTH, FRAME_RATE

from game import Game


if __name__ == "__main__":
    # init colorama
    init()

    # initialize game
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE)

    try:
        signal.signal(signal.SIGINT, lambda *a: 1 / 0)

        # hide cursor
        stdout.write("\033[?25l")
        stdout.flush()

        # play game
        game.play()

    except:
        # deinit colorama
        deinit()

        # show cursor
        stdout.write("\033[?25h \x1b[H")
        stdout.flush()
