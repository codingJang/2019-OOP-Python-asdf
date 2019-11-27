import pygame
from yejun.blit_methods import center_blit


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/missile1.png')
        self.display_image = self.image
        self.rect = self.display_image.get_rect().move(x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.trans_speed = 9
        self.rot_speed = 2
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(self.trans_speed, 0)

    def update(self, screen, plane_loc, plane_vel):
        plane_vec = pygame.math.Vector2(plane_loc - self.loc)
        if self.vel.cross(plane_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        _, theta = self.vel.as_polar()
        self.display_image = pygame.transform.rotate(self.image, -theta - 90)
        self.loc += self.vel - plane_vel
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        center_blit(screen, self)
