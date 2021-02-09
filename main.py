from sys import stdout
from surface import Surface
from entity import Entity

if __name__ == "__main__":
    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize surface
    surface = Surface(framerate=0.03, borders=True)

    # entities
    aster = Entity(position=(2, 2), velocity=(0, 1))
    surface.register(aster)

    circ = Entity(velocity=(1, 1), sprite="o")
    surface.register(circ)

    amper = Entity(position=(3, 3), velocity=(1, 0), sprite="&")
    surface.register(amper)

    # blit surface
    surface.blit()
