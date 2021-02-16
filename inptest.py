import sys
import tty
import termios


raw_input = RawInput()

while True:
    pressed = raw_input.get()
    if pressed == "b":
        print("bruh")
