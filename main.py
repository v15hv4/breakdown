from sys import stdout
from surface import Surface
from entity import Entity

if __name__ == "__main__":
    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize surface
    surface = Surface(framerate=0.1, borders=True)

    # entities
    wall = Entity(dimens=(15, 2), position=(8, 10), velocity=(0, 0), sprite="H")
    surface.register(wall)

    aster = Entity(position=(2, 2), velocity=(1, 1))
    surface.register(aster)

    # blit surface
    surface.blit()
