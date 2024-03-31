"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-condition: Karel is on the left side of the wall, facing East.
    post-condition: Karel is on the right side of the wall.
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition: Karel is on the left side of the wall, facing East.
    post-condition: Karel is facing North.
    """
    turn_left()
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """
    Karel will cross the wall from left to right.
    """
    turn_right()
    move()


def down():
    """
    pre-condition: Karel is on the upper right side of the wall, facing South.
    post-condition: karel is on the lower right side of the wall, facing East.
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
