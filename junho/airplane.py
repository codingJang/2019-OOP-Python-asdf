import pygame
from yejun.blit_methods import center_blit


class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('images/airplane1.png')
        self.display_image = self.image
        self.rect = self.display_image.get_rect().move(x, y)
        self.width = self.image.get_width()/2
        self.height = self.image.get_height()/2
        self.trans_speed = 6
        self.rot_speed = 3
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(self.trans_speed, 0)
        self.cnt = 0
        self.mode = 'forward'

    def update(self, screen, events):
        for event in events:
            if event.type == pygame.KEYDOWN:  # KEYDOWN 이벤트 발생
                if event.key == pygame.K_LEFT:  # left 를 눌렀다면
                    self.mode = 'left'
                    self.cnt += 1
                if event.key == pygame.K_RIGHT:  # right 를 눌렀다면
                    self.mode = 'right'
                    self.cnt += 1
            if event.type == pygame.KEYUP:  # 키보드에서 손가락을 떼면
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    self.cnt -= 1
        if self.cnt == 0 or self.cnt == 2:
            self.mode = 'forward'
        if self.mode == 'left':
            delta_theta = -self.rot_speed
        if self.mode == 'right':
            delta_theta = self.rot_speed
        if self.mode == 'forward':
            delta_theta = 0
        self.vel = self.vel.rotate(delta_theta)
        _, theta = self.vel.as_polar()
        self.display_image = pygame.transform.rotate(self.image, -90 - theta)
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        center_blit(screen, self)
