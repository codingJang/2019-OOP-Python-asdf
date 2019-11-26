import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.length = 800
        self.image = pygame.image.load("yurim/background.png")

    def moving(self, plane_vel):
        self.x -= plane_vel.x
        self.y -= plane_vel.y
        if self.x < -self.length:
            self.x = self.length
        elif self.x > self.length:
            self.x = -self.length
        if self.y < -self.length:
            self.y = self.length
        elif self.y > self.length:
            self.y = -self.length
