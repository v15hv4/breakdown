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
    aster = Entity(position=(2, 2), velocity=(1, 1))
    surface.register(aster)

    circ = Entity(position=(20, 20), velocity=(-1, -1), sprite="o")
    surface.register(circ)

    # blit surface
    surface.blit()
