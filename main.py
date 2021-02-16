from sys import stdout
from colorama import init, Fore

from game import Game
from entity import Entity
from ball import Ball
from brick import Brick

if __name__ == "__main__":
    # init colorama
    init()

    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize game
    game = Game()

    # entities
    brick1 = Brick(id="brick1", dimens=(65, 1), position=(1, 10), color=Fore.GREEN)
    game.register(brick1)

    brick2 = Brick(id="brick2", dimens=(65, 1), position=(20, 20), color=Fore.BLUE)
    game.register(brick2)

    # aster = Entity(id="aster", position=(2, 2), velocity=(1, 1))
    # game.register(aster)

    # amper = Entity(id="amper", position=(4, 4), velocity=(0, 1), sprite="&")
    # game.register(amper)

    ball = Ball(velocity=(1, 1))
    game.register(ball)

    # play game
    game.play()
