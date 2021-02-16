from sys import stdout

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
    game = Game(framerate=10)

    # bricks
    brick1 = Brick(id="brick1", dimens=(65, 1), position=(1, 10), color=Fore.GREEN)
    game.register(brick1)

    brick2 = Brick(id="brick2", dimens=(65, 1), position=(20, 20), color=Fore.BLUE)
    game.register(brick2)

    brick3 = Brick(id="brick3", dimens=(2, 2), position=(30, 30), color=Fore.CYAN)
    game.register(brick3)

    # paddle
    paddle = Paddle(position=((game.width // 2) - 3, game.height - 2))
    game.register(paddle)

    # ball
    ball = Ball(velocity=(1, 1))
    game.register(ball)

    # try:
    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # play game
    game.play()

    # except:
    #     # show cursor
    #     stdout.write("\033[?25h")
    #     stdout.flush()
