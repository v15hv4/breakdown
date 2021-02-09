from sys import stdout
from colorama import init

from surface import Surface
from entity import Entity
from ball import Ball

if __name__ == "__main__":
    # init colorama
    init()

    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize surface
    surface = Surface(framerate=0.03)

    # entities
    wall = Entity(id="wall", dimens=(15, 2), position=(8, 10), velocity=(0, 0), sprite="H")
    surface.register(wall)

    aster = Entity(id="player", position=(2, 2), velocity=(1, 1))
    surface.register(aster)

    amper = Entity(id="player", position=(4, 4), velocity=(0, 1), sprite="&")
    surface.register(amper)

    ball = Ball()
    surface.register(ball)

    # blit surface
    surface.blit()
