import os

FRAME_RATE = 22

# screen properties
SCREEN_WIDTH = os.get_terminal_size().columns + 1
SCREEN_HEIGHT = os.get_terminal_size().lines

# brick properties
BRICK_LINE_COUNT = 8
BRICK_WIDTH = SCREEN_WIDTH // 9
BRICK_PADDING = (SCREEN_WIDTH - (BRICK_WIDTH * BRICK_LINE_COUNT)) // 2
BRICK_LAYOUT = [  # format: (health, powerup)
    [(4, None), (3, None), (2, None), (1, None), (1, None), (2, None), (3, None), (4, None)],
    [(3, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (3, None)],
    [(2, None), (3, None), (4, None), (3, None), (3, None), (4, None), (3, None), (2, None)],
    [(1, None), (2, None), (3, None), (1, None), (0, None), (3, None), (2, None), (1, None)],
    [(1, None), (2, None), (3, None), (0, None), (1, None), (3, None), (2, None), (1, None)],
    [(2, None), (3, None), (4, None), (3, None), (3, None), (4, None), (3, None), (2, None)],
    [(3, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (3, None)],
    [(4, None), (3, None), (2, None), (1, None), (1, None), (2, None), (3, None), (4, None)],
]

# paddle properties
PADDLE_WIDTH = SCREEN_WIDTH // 3
PADDLE_VELOCITY = (PADDLE_WIDTH // 8, 0)

# ball properties
BALL_POSITION = (20, 20)
BALL_VELOCITY = (1, 1)
