from sys import stdout
from surface import Surface
from entity import Entity

if __name__ == "__main__":
    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize surface
    surface = Surface(borders=True)

    # entities
    aster = Entity()
    surface.register(aster)

    # blit surface
    surface.blit()
