import os

# game framerate
FRAME_RATE = 20

# screen properties
SCREEN_WIDTH = os.get_terminal_size().columns + 1
SCREEN_HEIGHT = os.get_terminal_size().lines

# level properties
FALLING_THRESHOLD = 20

# brick properties
BRICK_LINE_COUNT = 8
BRICK_WIDTH = SCREEN_WIDTH // 9
BRICK_PADDING = (SCREEN_WIDTH - (BRICK_WIDTH * BRICK_LINE_COUNT)) // 2
BRICK_RAINBOW_CHANCE = 1

# paddle properties
PADDLE_WIDTH = SCREEN_WIDTH // 3
PADDLE_VELOCITY = (PADDLE_WIDTH // 8, 0)

# ball properties
BALL_POSITION = (20, 20)
BALL_VELOCITY = (0, -1)

# sound
SOUND_ENABLED = True
