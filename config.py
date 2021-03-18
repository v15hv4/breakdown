import os

FRAME_RATE = 22

# screen properties
SCREEN_WIDTH = os.get_terminal_size().columns + 1
SCREEN_HEIGHT = os.get_terminal_size().lines

# level properties
LEVEL_LAYOUT_1 = [  # format: (health, powerup)
    [(4, None), (3, None), (2, "SP"), (1, None), (1, None), (2, None), (3, None), (4, None)],
    [(3, None), (4, "EP"), (3, None), (2, None), (2, None), (3, None), (4, "SP"), (3, None)],
    [(2, None), (3, None), (4, None), (3, "EP"), (3, None), (4, None), (3, None), (2, None)],
    [(1, None), (2, None), (3, None), (1, None), (0, "EP"), (3, None), (2, None), (1, None)],
    [(1, None), (2, None), (3, None), (0, None), (1, None), (3, None), (2, None), (1, "EP")],
    [(2, "EP"), (3, None), (4, None), (3, None), (3, None), (4, None), (3, None), (2, None)],
    [(3, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (3, None)],
    [(4, None), (3, "EP"), (2, None), (1, "EP"), (1, None), (2, "SP"), (3, None), (4, None)],
]

LEVEL_LAYOUT_2 = [  # format: (health, powerup)
    [(4, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (4, None)],
    [(4, None), (3, None), (3, None), (2, None), (2, None), (3, None), (3, None), (4, None)],
    [(3, None), (3, None), (0, None), (1, None), (1, None), (0, None), (3, None), (3, None)],
    [(2, None), (2, None), (1, None), (1, None), (1, None), (1, None), (2, None), (2, None)],
    [(2, None), (2, None), (1, None), (1, None), (1, None), (1, None), (2, None), (2, None)],
    [(3, None), (3, None), (0, None), (1, None), (1, None), (0, None), (3, None), (3, None)],
    [(4, None), (3, None), (3, None), (2, None), (2, None), (3, None), (3, None), (4, None)],
    [(4, None), (4, None), (3, None), (2, None), (2, None), (3, None), (4, None), (4, None)],
]

LEVEL_LAYOUT_3 = [  # format: (health, powerup)
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [(0, None), None, None, (0, None), (0, None), None, None, (0, None)],
]

# LEVEL_LAYOUT_1 = LEVEL_LAYOUT_2 = LEVEL_LAYOUT_3 = [  # format: (health, powerup)
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, None, None, None],
#     [None, None, None, None, None, (1, None), None, None],
# ]

FALLING_THRESHOLD = 20


# brick properties
BRICK_LINE_COUNT = 8
BRICK_WIDTH = SCREEN_WIDTH // 9
BRICK_PADDING = (SCREEN_WIDTH - (BRICK_WIDTH * BRICK_LINE_COUNT)) // 2

# paddle properties
PADDLE_WIDTH = SCREEN_WIDTH // 3
PADDLE_VELOCITY = (PADDLE_WIDTH // 8, 0)

# ball properties
BALL_POSITION = (20, 20)
BALL_VELOCITY = (1, 1)
