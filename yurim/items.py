import pygame
import random
from yejun.methods import *

__all__ = ['Item', 'make_items']


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.loc = None  # pygame.math.Vector2
        self.image = None
        self.display_image = None
        self.rect = None
        self.mask = None
        self.width = None
        self.height = None
        self.time = 0
        self.kill_time = None
        self.set_location(x, y)
        self.set_image('images/star.png')  # 이미지 고르고 위치 설정
        self.set_kill_time(1800)  # kill time 설정

    def set_location(self, x, y):  # 초기 위치 및 방향 설정
        self.loc = pygame.math.Vector2(x, y)

    def set_image(self, path):  # 이미지 고르고 위치 설정
        self.image = pygame.image.load(path)
        self.display_image = self.image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = center_rect(self)
        self.mask = pygame.mask.from_surface(self.display_image)

    def set_kill_time(self, kill_time):
        self.kill_time = kill_time

    def update(self, screen, plane_vel):
        self.loc -= plane_vel
        self.rect = center_rect(self)
        self.mask = pygame.mask.from_surface(self.display_image)
        center_blit(screen, self)
        self.time += 1
        if self.time >= self.kill_time:
            self.kill()


def make_items(sprites, time):
    ran_num = random.randint(1, 100)
    if time % 3 == 0 and ran_num > 95:
        sprites.add(Item(random.randint(0, 800), random.randint(0, 800)))
