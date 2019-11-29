import pygame
import random
from yejun.missile import *


def add_missile(sprites, level):
    if level < 2:
        level = 2
    while len(sprites) < level:
        ran_num = random.randint(1, 3)
        ran_x = 100*random.randint(1, 9)
        ran_y = 800*random.randint(0, 2)

        if ran_num == 1:
            sprites.add(MiniMissile(ran_x, ran_y, 0))
        elif ran_num == 2:
            sprites.add(DrunkMissile(ran_x, ran_y, 0))