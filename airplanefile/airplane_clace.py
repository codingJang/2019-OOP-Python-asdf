import pygame
from math import fabs

screen_w, screen_h = 800, 800


class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('jet2.png')
        self.display_image = None
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.trans_speed = 1.5
        self.rot_speed = 1.5
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(self.trans_speed, 0)

    def update(self, mode):
        if

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if mode == 'left':
                    # 1
                    delta = self.rot_speed
                    cnt += 1
                if event.key == pygame.K_RIGHT:
                    # -1
                    delta = -self.rot_speed
                    cnt += 1
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    cnt -= 1
        if cnt == 0:
            delta = 0
        angle += delta
        rotated_image = pygame.transform.rotate(my_image, angle)
        w = my_image.get_width()
        h = my_image.get_height()
        rw = rotated_image.get_width()
        rh = rotated_image.get_height()


        if self.vel.cross(mouse_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        self.X += self.vel
        self.display_image = pygame.transform.rotate(self.image, -vel_theta)

