import pygame


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/ufo.png')
        self.display_image = None
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.trans_speed = 3
        self.rot_speed = 1
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(self.trans_speed, 0)

    def update(self, plane_loc, plane_vel):
        plane_vec = pygame.math.Vector2(plane_loc - self.loc)
        if self.vel.cross(plane_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        _, theta = self.vel.as_polar()
        self.display_image = pygame.transform.rotate(self.image, -theta)
        self.loc += self.vel - plane_vel
