"""
File: PotholeFilling.py
Name: Jonathan
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    TODO:
    """
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    """
    pre-condition: Karel is on the upper left of the pothole, facing East.
    post-condition: Karel is in the pothole, facing South.
    """
    move()
    turn_right()
    move()


def put_99_beepers():
    for i in range(99):
        put_beeper()


def go_out():
    """
    pre-condition: Karel is in the pothole, facing South.
    post-condition: Karel is on the upper left of the pothole, facing East.
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
