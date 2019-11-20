import pygame


class Missile(pygame.sprite.Sprite):  # 기본 미사일 클래스
    def __init__(self, x, y):
        super().__init__()  # pygame.sprite.Sprite 의 __init__() 실행
        self.image = pygame.image.load('images/ufo.png')  # 이미지 설정
        self.display_image = self.image  # display_image: 실시간으로 디스플레이되는 이미지
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.trans_speed = 3  # 병진 속력
        self.loc = pygame.math.Vector2(x, y)  # 위치 벡터
        self.vel = pygame.math.Vector2(self.trans_speed, 0)  # 속도 벡터

    def update(self, plane_loc, plane_vel):
        plane_vec = pygame.math.Vector2(plane_loc - self.loc)
        if self.vel.cross(plane_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        _, theta = self.vel.as_polar()
        self.display_image = pygame.transform.rotate(self.image, -theta)
        self.loc += self.vel - plane_vel


class TrackingMissile(Missile):
    def __init__(self, x, y):
        super().__init__()  # Missile 기본 클래스의 __init__() 실행
        self.rot_speed = 1  # 회전 속력

    def update(self, plane_loc, plane_vel):
        plane_vec = pygame.math.Vector2(plane_loc - self.loc)
        if self.vel.cross(plane_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        _, theta = self.vel.as_polar()
        self.display_image = pygame.transform.rotate(self.image, -theta)
        self.loc += self.vel - plane_vel
