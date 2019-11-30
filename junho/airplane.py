import pygame
from yejun.methods import *

__all__ = ['Airplane', 'Jetplane', 'Spaceship']


class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = None
        self.display_image = None
        self.rect = None
        self.mask = None
        self.width = None
        self.height = None
        self.trans_speed = None
        self.rot_speed = None
        self.loc = None
        self.vel = None
        self.cnt = None
        self.set_speeds(6, 3)
        self.set_initial(x, y, angle)
        self.set_image('images/airplane1.png')

    def set_speeds(self, trans_speed, rot_speed):  # 병진, 회전 속력 설정
        self.trans_speed = trans_speed
        self.rot_speed = rot_speed

    def set_initial(self, x, y, angle):  # 초기 위치 및 방향 설정
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.vel.from_polar((self.trans_speed, angle))
        self.cnt = 0

    def set_image(self, path):  # 이미지 고르고 위치 설정
        self.image = pygame.image.load(path)
        self.display_image = self.image
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        self.mask = pygame.mask.from_surface(self.display_image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, screen, pic=None, pause=False):
        pressed = pygame.key.get_pressed()
        right = pressed[pygame.K_RIGHT]
        left = pressed[pygame.K_LEFT]
        if right and left:
            delta_theta = 0
        elif right:
            delta_theta = self.rot_speed
        elif left:
            delta_theta = -self.rot_speed
        else:
            delta_theta = 0

        if not pause:
            self.vel = self.vel.rotate(delta_theta)
            _, theta = self.vel.as_polar()
            self.display_image = pygame.transform.rotate(self.image, -90 - theta)
            self.rect = center_rect(self)
            self.mask = pygame.mask.from_surface(self.display_image)
            center_blit(screen, self)


class Jetplane(Airplane):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.set_speeds(7, 2)
        self.set_initial(x, y, angle)
        self.set_image("images/airplane2.png")


class Spaceship(Airplane):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.set_speeds(5, 4)
        self.set_initial(x, y, angle)
        self.set_image("images/airplane3.png")
