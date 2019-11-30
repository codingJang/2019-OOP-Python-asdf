import pygame
import random


class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)
        self.time = 0
        self.kill_time = None
        self.set_kill_time(180)
        self.image = None
        self.display_image = None
        self.rect = None
        self.width = None
        self.height = None
        self.time = 0
        self.set_image('images/star.png')  # 이미지 고르고 위치 설정
        self.set_kill_time(1800)  # kill time 설정

    def set_image(self, path):  # 이미지 고르고 위치 설정
        self.image = pygame.image.load(path)
        self.display_image = self.image
        self.rect = self.display_image.get_rect().move(self.x, self.y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def set_kill_time(self, kill_time):
        self.kill_time = kill_time

    def update(self, screen, plane_vel):
        self.x -= plane_vel.x
        self.y -= plane_vel.y
        screen.blit(self.image, (self.x, self.y))
        self.time += 1
        if self.time >= self.kill_time:
            self.kill()


def make_items(sprites, time):
    ran_num = random.randint(1, 100)
    if time % 3 == 0 and ran_num >95:
        sprites.add(Item())
