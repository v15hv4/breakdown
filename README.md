# breakdown
> A terminal based Breakout clone written in Python, with no curses libraries.  

![preview](https://media.discordapp.net/attachments/785528722882560030/813787321941229570/unknown.png)

## About
The player will be using a paddle with a bouncing ball to smash awall of bricks and make high scores! The objective of the game is to break all the bricks as fast as possible and beat the highest score! You lose a life when the ball touches the ground below the paddle.

## Requirements
- Python3

## How to play
- Install dependencies: `pip install -r requirements.txt`
- Run the game: `python main.py`

## Keybindings
[W]: Start Level  
[A]: Move Paddle Left  
[D]: Move Paddle Right  
[L]: Skip Level

#### Note
Run the game using `xset r rate 1; python main.py; xset r rate 660 25` to adjust your keyboard's repeat rate for a smoother experience.
