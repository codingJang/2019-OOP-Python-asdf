import pygame
from math import fabs


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('ufo.png')
        self.display_image = None
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.trans_speed = 0.2
        self.rot_speed = 0.2
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(self.trans_speed, 0)

    def update(self):
        mouse_loc = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_vec = pygame.math.Vector2(mouse_loc - self.loc)
        _, vel_theta = self.vel.as_polar()
        if self.vel.cross(mouse_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        self.loc += self.vel
        self.display_image = pygame.transform.rotate(self.image, -vel_theta)
