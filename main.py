from sys import stdout
from random import randint

from colorama import Fore, init

from ball import Ball
from brick import Brick
from entity import Entity
from game import Game
from paddle import Paddle

if __name__ == "__main__":
    # init colorama
    init()

    # initialize game
    game = Game(framerate=24)

    # bricks
    BRICK_WIDTH = 8
    SCREEN_PADDING = 7
    for i in range(8):
        for j in range(5):
            brick = Brick(
                id=f"brick{i}{j}",
                dimens=(BRICK_WIDTH, 1),
                position=(SCREEN_PADDING + (i * BRICK_WIDTH) + 2 * i, 3 + (2 * j)),
                health=randint(1, 4),
            )
            game.register(brick)

    # paddle
    PADDLE_WIDTH = 30
    paddle = Paddle(
        dimens=(PADDLE_WIDTH, 1),
        position=((game.width // 2) - (PADDLE_WIDTH // 2), game.height - 2),
    )
    game.register(paddle)

    # ball
    ball = Ball(position=(20, 20), velocity=(1, 1))
    game.register(ball)

    try:
        # hide cursor
        stdout.write("\033[?25l")
        stdout.flush()

        # play game
        game.play()

    except:
        # show cursor
        stdout.write("\033[?25h")
        stdout.flush()
