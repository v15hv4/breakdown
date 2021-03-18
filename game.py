import os, sys, tty, time, random, signal, termios

from colorama import Fore, Back
from entity import Entity
from brick import Brick
from paddle import Paddle
from ball import Ball

from config import *


def getchar():
    # get currently pressed key
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


class TimeoutException(Exception):
    pass


def timeoutException(*args):
    raise TimeoutException


class Game:
    def __init__(self, width, height, framerate=60) -> None:
        self.height = height
        self.width = width
        self.framerate = framerate
        self.entities = []
        self.board = []
        self.start_time = time.time()
        self.remaining_lives = 3
        self.score = 0
        self.pressed = None
        self.game_over = False
        self.playing = False
        self.level = 1

        self.cursor = {
            "RESET": lambda: f"\x1b[H",
            "DOWN": lambda n: f"\x1b[{n}B",
            "RIGHT": lambda n: f"\x1b[{n}C",
        }

        # handle game over signal
        signal.signal(signal.SIGUSR1, self.end_game)

        # handle level start signal
        signal.signal(signal.SIGUSR2, self.start_level)

        # handle level skip signal
        signal.signal(signal.SIGTRAP, self.next_level)

    def set_up_level(self, level) -> None:
        if level == 0:
            return

        self.entities = []
        BRICK_LAYOUT = [LEVEL_LAYOUT_1, LEVEL_LAYOUT_2, LEVEL_LAYOUT_3][level - 1]

        # bricks
        for i in range(BRICK_LINE_COUNT):
            for j in range(BRICK_LINE_COUNT):
                if BRICK_LAYOUT[j][i]:
                    brick = Brick(
                        id=f"brick{i}{j}",
                        dimens=(BRICK_WIDTH, 1),
                        position=(BRICK_PADDING + (i * BRICK_WIDTH), 6 + j),
                        health=BRICK_LAYOUT[j][i][0],
                        powerup=BRICK_LAYOUT[j][i][1],
                        rainbow=(BRICK_LAYOUT[j][i][0] > 0)
                        and (random.randint(0, 9) < BRICK_RAINBOW_CHANCE),
                    )
                    self.register(brick)

        # paddle
        paddle = Paddle(
            dimens=(PADDLE_WIDTH, 1),
            position=((self.width // 2) - (PADDLE_WIDTH // 2), self.height - 2),
        )
        self.register(paddle)

        # ball
        ball = Ball()
        self.register(ball)

    def start_game(self, *args, **kwargs) -> None:
        if self.remaining_lives <= 0:
            self.remaining_lives = 3
            self.score = 0
            self.game_over = False

    def start_level(self, *args, **kwargs) -> None:
        if not self.playing:
            ball = list(filter(lambda e: type(e).__name__ == "Ball", self.entities))[0]
            ball.reset()
            ball.start()
            self.start_time = time.time()
            self.playing = True

    def next_level(self, *args, **kwargs) -> None:
        self.level = (self.level + 1) % 4
        self.end_level()
        self.set_up_level(self.level)

    def end_level(self) -> None:
        ball = list(filter(lambda e: type(e).__name__ == "Ball", self.entities))[0]
        ball.reset()
        self.playing = False

    def end_game(self, *args, **kwargs):
        self.remaining_lives -= 1

        if self.remaining_lives > 0:
            self.start_game()
        else:
            self.game_over = True

        self.end_level()

    def increment_score(self) -> None:
        self.score += 100

    def reset(self) -> None:
        self.board = [[None for _ in range(self.width)] for _ in range(self.height)]

        border_topleft = Entity(sprite="┌")
        border_topright = Entity(sprite="┐")
        border_horizontal = Entity(sprite="─")
        border_vertical = Entity(sprite="│")

        # draw borders
        for i in range(self.height):
            for j in range(self.width):
                # sides
                if j in [0, self.width - 1]:
                    self.board[i][j] = border_vertical

                # top
                if i == 0:
                    if j == 0:
                        self.board[i][j] = border_topleft
                    elif j == self.width - 1:
                        self.board[i][j] = border_topright
                    else:
                        self.board[i][j] = border_horizontal

    def register(self, entity) -> None:
        self.entities.append(entity)

    def unregister(self, entity) -> None:
        self.entities = list(filter(lambda e: e.id != entity.id, self.entities))

    def blit_completed(self) -> None:
        os.system("clear")
        message = f"""
{" " * ((self.width // 2) - 8)}      YOU WIN!

{" " * ((self.width // 2) - 8)}         ⢀⣀⣀⣄⣶⡶⣦⣀       
{" " * ((self.width // 2) - 8)}    ⢠⡦⡟⠻⠛⠙⠉⠈⠄⠄⠈⠻⠛⣾⣦⣤⣀  
{" " * ((self.width // 2) - 8)}  ⣰⡿⠟⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠋⠽⢿⣧ 
{" " * ((self.width // 2) - 8)}⢀⣴⠞⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢼⠆ 
{" " * ((self.width // 2) - 8)}⣼⠇⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣶⣿⣶⣦⣤⣀⠄⣻⡃ 
{" " * ((self.width // 2) - 8)}⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⢸⣧ 
{" " * ((self.width // 2) - 8)}⢿⡀⠄⠄⠄⠄⠄⠄⠄⢠⣾⣿⣿⣋⣩⣭⣝⣿⣿⠛⢰⡇ 
{" " * ((self.width // 2) - 8)}⢸⡇⠄⠄⢀⠄⠄⠄⠄⣾⣿⣿⣿⣟⣯⠉⢉⣿⠋⣟⢻⡇ 
{" " * ((self.width // 2) - 8)} ⢹⡀⢳⡗⠂⣠⠄⠄⣿⣿⣿⣿⣿⣭⣽⣿⣿⣿⣉⣸⠇ 
{" " * ((self.width // 2) - 8)} ⠈⣷⠄⢳⣷⣿⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇ 
{" " * ((self.width // 2) - 8)}  ⠘⣧⠄⠈⠙⠄⠄⠄⠉⠙⠛⠛⣿⣿⣷⣤⣄⢿⡿⠃ 
{" " * ((self.width // 2) - 8)}   ⠉⠳⣄⡀⠄⠄⠄⢢⣦⣾⣿⠿⠿⠛⠉⢉⣽⠇  
{" " * ((self.width // 2) - 8)}     ⠘⠿⣄⢀⠄⣀⣝⢻⣿⡿⠒⣀⣀⣸⠁   
{" " * ((self.width // 2) - 8)}       ⠈⠳⣤⠁⠙⠎⢻⣄⠄⠄⣸⠋    
{" " * ((self.width // 2) - 8)}         ⠈⠙⠶⢦⣄⣀⣣⠴⠃     

{" " * ((self.width // 2) - 8)}      SCORE: {self.score}

{" " * ((self.width // 2) - 8)}   Press Esc to quit.
        """

        sys.stdout.write("\n" * (self.height // 4))
        sys.stdout.write(" " * ((self.width // 2) - (len(message) // 2)))
        sys.stdout.write(message)
        sys.stdout.flush()
        sys.stdout.write(self.cursor["RESET"]())

        # exit game
        if self.pressed == "\x1b":
            signal.raise_signal(2)

    def blit_gameover(self) -> None:
        os.system("clear")
        message = f"""
{" " * ((self.width // 2) - 10)}      GAME OVER!

{" " * ((self.width // 2) - 10)}⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⣿⣿⣿⠦⠀⠸⣿⣿⡄⢻
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⢻⠇⣼
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⠀⠀noob⠀ ⡟⣰
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣼⢀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
{" " * ((self.width // 2) - 10)}⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿
{" " * ((self.width // 2) - 10)}⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸
{" " * ((self.width // 2) - 10)}⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸

{" " * ((self.width // 2) - 10)}      SCORE: {self.score}

{" " * ((self.width // 2) - 10)}   Press Esc to quit.
        """

        sys.stdout.write("\n" * (self.height // 4))
        sys.stdout.write(" " * ((self.width // 2) - (len(message) // 2)))
        sys.stdout.write(message)
        sys.stdout.flush()
        sys.stdout.write(self.cursor["RESET"]())

        # exit game
        if self.pressed == "\x1b":
            signal.raise_signal(2)

    def blit(self) -> None:
        current_time = int(round(time.time() - self.start_time, 0))

        # update game state
        level_incomplete = 0
        self.reset()
        for entity in self.entities:
            # check for level clearance
            if type(entity).__name__ == "Brick" and entity.health > 0:
                level_incomplete += 1

            # update powerup status
            if hasattr(entity, "active_powerup"):
                if (entity.active_powerup.expires <= time.time()) or not level_incomplete:
                    entity.active_powerup.deactivate(entity)

            y, x = entity.position
            entity.move(self)
            for h in range(entity.dimens[1]):
                for w in range(entity.dimens[0]):
                    self.board[x + h][y + w] = entity

        # render current game state
        for i in range(self.height):
            for j in range(self.width):
                sys.stdout.write(self.cursor["RESET"]())
                sys.stdout.write(f"{self.cursor['DOWN'](i - 1)}{self.cursor['RIGHT'](j - 1)}")

                if i == 2 and (1 < j < self.width - 1):
                    # display time & lives
                    if j == 3:
                        sys.stdout.write(f"TIME: {current_time:05}   LIVES: {self.remaining_lives}")

                    # display level & score
                    if j == self.width - (20 + len(str(self.score))):
                        sys.stdout.write(f"LEVEL: {self.level}   SCORE: {self.score}")

                # display entities
                elif self.board[i][j]:
                    sys.stdout.write(
                        f"{self.board[i][j].color}{self.board[i][j].sprite}{Fore.RESET}"
                    )

                else:
                    sys.stdout.write(" ")

                if not self.playing and not self.game_over:
                    sys.stdout.write(self.cursor["RESET"]())
                    sys.stdout.write(
                        f"{self.cursor['DOWN'](self.height // 2)}{self.cursor['RIGHT']((self.width // 2) - 6)}"
                    )
                    sys.stdout.write("Press W to start.")

            sys.stdout.flush()
        sys.stdout.write(self.cursor["RESET"]())

        if not level_incomplete:
            self.next_level()
            return

        # start level
        if self.pressed == "w":
            signal.raise_signal(12)

        # skip level backdoor
        if self.pressed == "l":
            signal.raise_signal(5)

    def play(self) -> None:
        interval = 1 / self.framerate
        os.system("clear")
        last_pressed = 0

        if not self.playing:
            self.set_up_level(self.level)

        while True:
            try:
                signal.setitimer(signal.ITIMER_REAL, interval)
                signal.signal(signal.SIGALRM, timeoutException)
                if self.game_over:
                    self.blit_gameover()
                elif self.level == 0:
                    self.blit_completed()
                else:
                    self.blit()
                self.pressed = getchar()
                last_pressed = time.time_ns()
            except TimeoutException:
                self.pressed = None
