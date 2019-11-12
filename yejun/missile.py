import pygame
from math import fabs

screen_w, screen_h = 800, 800


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ufo.png')
        self.display_image = None
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.trans_speed = 0.2
        self.rot_speed = 0.2
        self.loc = pygame.math.Vector2(screen_w / 2 - self.w / 2, screen_h / 2 - self.h / 2)
        self.vel = pygame.math.Vector2(self.speed, 0)

    def update(self):
        mouse_loc = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_vec = pygame.math.Vector2(mouse_loc - self.loc)
        _, vel_theta = self.vel.as_polar()
        if self.vel.cross(mouse_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        self.X += self.vel
        self.display_image = pygame.transform.rotate(self.image, -vel_theta)
