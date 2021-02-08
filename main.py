from sys import stdout
from surface import Surface

if __name__ == "__main__":
    # hide cursor
    stdout.write("\033[?25l")
    stdout.flush()

    # initialize and blit
    surface = Surface(borders=True)
    surface.blit()
