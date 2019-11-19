import pygame


class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/jet2.png')
        self.display_image = self.image
        self.width = self.image.get_width()/2
        self.height = self.image.get_height()/2
        self.trans_speed = 1.5
        self.rot_speed = 3
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(self.trans_speed, 0)

    def update(self, mode):
        if mode == 'left':
            delta_theta = -self.rot_speed
        if mode == 'right':
            delta_theta = self.rot_speed
        if mode == 'forward':
            delta_theta = 0
        self.vel = self.vel.rotate(delta_theta)
        _, theta = self.vel.as_polar()
        self.display_image = pygame.transform.rotate(self.image, -90 - theta)
        self.rw = self.display_image.get_width()/2
        self.rh = self.display_image.get_height()/2
