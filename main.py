import os, sys, signal

from colorama import Fore, init, deinit
from game import Game

from config import SCREEN_HEIGHT, SCREEN_WIDTH, FRAME_RATE


if __name__ == "__main__":
    # init colorama
    init()

    # initialize game
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE)

    try:
        signal.signal(signal.SIGINT, lambda *a: 1 / 0)

        # hide cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

        # play game
        game.play()

    except:
        # deinit colorama
        deinit()

        # show cursor
        sys.stdout.write("\033[?25h \x1b[H")
        sys.stdout.flush()
