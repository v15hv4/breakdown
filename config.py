import os

FRAME_RATE = 20

# screen properties
SCREEN_WIDTH = os.get_terminal_size().columns + 1
SCREEN_HEIGHT = os.get_terminal_size().lines

# brick properties
BRICK_WIDTH = SCREEN_WIDTH // 9
BRICK_PADDING = (SCREEN_WIDTH - (BRICK_WIDTH * 8)) // 2

# paddle properties
PADDLE_WIDTH = SCREEN_WIDTH // 3
PADDLE_VELOCITY = (PADDLE_WIDTH // 8, 0)

# ball properties
BALL_POSITION = (20, 20)
BALL_VELOCITY = (1, 1)
