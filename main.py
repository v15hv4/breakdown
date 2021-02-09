from sys import stdout
from surface import Surface
from entity import Entity

if __name__ == "__main__":
    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize surface
    surface = Surface(framerate=0.03)

    # entities
    wall = Entity(name="wall", dimens=(15, 2), position=(8, 10), velocity=(0, 0), sprite="H")
    surface.register(wall)

    aster = Entity(name="player", position=(2, 2), velocity=(1, 1))
    surface.register(aster)

    circ = Entity(name="player", position=(1, 1), velocity=(1, 0), sprite="o")
    surface.register(circ)

    amper = Entity(name="player", position=(4, 4), velocity=(0, 1), sprite="&")
    surface.register(amper)

    # blit surface
    surface.blit()
