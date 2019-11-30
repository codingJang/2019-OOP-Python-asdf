import pygame
import random


class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 800)
        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect().move(self.x, self.y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.time = 0
        self.kill_time = None
        self.set_kill_time(180)

    def update(self, screen, plane_vel):
        self.x -= plane_vel.x
        self.y -= plane_vel.y
        screen.blit(self.image, (self.x, self.y))
        self.time += 1
        if self.time >= self.kill_time:
            self.kill()

    def set_kill_time(self, kill_time):
        self.kill_time = kill_time


def make_items(sprites, time):
    ran_num = random.randint(1, 100)
    if time % 3 == 0 and ran_num >95:
        sprites.add(Item())
