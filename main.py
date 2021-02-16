from sys import stdout
from colorama import init

from game import Game
from entity import Entity
from ball import Ball

if __name__ == "__main__":
    # init colorama
    init()

    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize game
    game = Game(framerate=0.1)

    # entities
    brick = Entity(id="brick", dimens=(15, 1), position=(8, 10), sprite="H")
    game.register(brick)

    # aster = Entity(id="aster", position=(2, 2), velocity=(1, 1))
    # game.register(aster)

    # amper = Entity(id="amper", position=(4, 4), velocity=(0, 1), sprite="&")
    # game.register(amper)

    ball = Ball()
    game.register(ball)

    # play game
    game.play()
