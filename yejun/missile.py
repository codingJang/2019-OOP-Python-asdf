import pygame
from yejun.blit_methods import center_blit


class Missile(pygame.sprite.Sprite):
    """
    기본 미사일 클래스
    미사일의 생성 및 비행기를 추적하는 기능을 포함함
    """
    def __init__(self, x, y, angle):
        """
        미사일 생성
        :param x: 초기 x (왼쪽에서부터 미사일 중심까지의 거리, 픽셀 단위)
        :param y: 초기 y (위쪽에서부터 미사일 중심까지의 거리, 픽셀 단위)
        :param angle: 초기 각도 (양의 x축 기준 시계 방향)
        """
        super().__init__()  # pygame.sprite.Sprite 클래스의 __init__ 실행
        # 사용할 변수들 선언
        self.trans_speed = None
        self.rot_speed = None
        self.loc = None  # pygame.math.Vector2
        self.vel = None  # pygame.math.Vector2
        self.image = None
        self.display_image = None
        self.rect = None
        self.width = None
        self.height = None
        self.set_speeds(7, 1.5)  # 병진 속도 7px/s, 회전 속도 1.5deg/s로 설정 (default)
        self.set_initial(x, y, angle)  # 초기 위치 및 바라보는 방향 설정
        self.set_image('images/missile_1.png')  # 이미지 고르고 위치 설정

    def set_speeds(self, trans_speed, rot_speed):  # 병진, 회전 속력 설정
        self.trans_speed = trans_speed
        self.rot_speed = rot_speed

    def set_initial(self, x, y, angle):  # 초기 위치 및 방향 설정
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.vel.from_polar((self.trans_speed, angle))

    def set_image(self, path):  # 이미지 고르고 위치 설정
        self.image = pygame.image.load(path)
        self.display_image = self.image
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, screen, plane_loc, plane_vel):  # update() 호출마다 위치 및 방향 리프레시
        plane_vec = pygame.math.Vector2(plane_loc - self.loc)
        if self.vel.cross(plane_vec) > 0:
            self.vel = self.vel.rotate(self.rot_speed)
        else:
            self.vel = self.vel.rotate(-self.rot_speed)
        _, theta = self.vel.as_polar()
        self.display_image = pygame.transform.rotate(self.image, -theta - 90)
        self.loc += self.vel - plane_vel
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        center_blit(screen, self)  # 중심을 기준으로 blit


class FastMissile(Missile):  # 좀 더 빠른 미사일
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.set_speeds(9, 1.5)
        self.set_initial(x, y, 0)
        self.set_image('images/missile2.png')


class DirectedMissile(Missile):  # 방향 전환을 하지 않고 직진하는 미사일
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.set_speeds(9, None)
        self.set_image('images/missile3.png')

    def update(self, screen, plane_loc, plane_vel):
        self.loc += self.vel - plane_vel
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        center_blit(screen, self)


class MiniMissile(Missile):  # 미니 미사일, 속도 느림
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.set_speeds(4, None)
        self.set_image('images/missile3.png')
