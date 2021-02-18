import os
import signal

from random import randint
from sys import stdout

from colorama import Fore, init, deinit

from config import *

from ball import Ball
from brick import Brick
from entity import Entity
from game import Game
from paddle import Paddle


if __name__ == "__main__":
    # init colorama
    init()

    # initialize game
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE)

    # bricks
    for i in range(8):
        for j in range(5):
            brick = Brick(
                id=f"brick{i}{j}",
                dimens=(BRICK_WIDTH, 1),
                position=(BRICK_PADDING + (i * BRICK_WIDTH), 3 + j),
                health=randint(1, 4),
            )
            game.register(brick)

    # paddle
    paddle = Paddle(
        dimens=(PADDLE_WIDTH, 1),
        position=((game.width // 2) - (PADDLE_WIDTH // 2), game.height - 2),
    )
    game.register(paddle)

    # ball
    ball = Ball(position=BALL_POSITION, velocity=BALL_VELOCITY)
    game.register(ball)

    try:
        signal.signal(signal.SIGINT, lambda *a: 1 / 0)

        # hide cursor
        stdout.write("\033[?25l")
        stdout.flush()

        # remove keyboard repeat delay
        os.system("xset r rate 1")

        # play game
        game.play()

    except:
        # show cursor
        stdout.write("\033[?25h \x1b[H")
        stdout.flush()

        # add back keyboard repeat delay
        os.system("xset r rate 660 25")

        # deinit colorama
        deinit()
