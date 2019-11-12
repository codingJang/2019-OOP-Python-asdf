import pygame


class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('jet2.png')
        self.display_image = self.image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.trans_speed = 1.5
        self.rot_speed = 1.5
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(self.trans_speed, 0)

    def update(self, mode):
        if mode == 'left':
            delta_theta = self.rot_speed
        if mode == 'right':
            delta_theta = -self.rot_speed
        if mode == 'straight':
            delta_theta = 0
        self.display_image = pygame.transform.rotate(self.display_image, delta_theta)
        self.vel = self.vel.rotate(delta_theta)

