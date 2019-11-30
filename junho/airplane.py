import pygame
from yejun.blit_methods import center_blit


class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = None
        self.display_image = None
        self.rect = None
        self.width = None
        self.height = None
        self.trans_speed = None
        self.rot_speed = None
        self.loc = None
        self.vel = None
        self.cnt = None
        self.mode = 'forward'
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
        self.width = self.image.get_width()
        self.height = self.image.get_height()

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
