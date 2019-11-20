"""
이유림이 반드시 참고해야 할 것...!!
****매우 중요****
대충 이런 flow 로 메인 코드가 개발되어야 협업이 편할 것 같음!
https://www.101computing.net/pygame-how-tos/
여기 이미지의 flow chart를 참고하시길
암튼 꼭 참고하세요
"""

import pygame  # pygame 가져오기
from yejun.missile import Missile  # 장예준이 만든 Missiles 클래스
from junho.airplane import Airplane  # 장준호가 만든 Airplanes 클래스


def center_blit(sprite):
    screen.blit(sprite.display_image,
                (sprite.loc.x - sprite.display_image.get_width()/2,
                 sprite.loc.y - sprite.display_image.get_height()/2))


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles!")

missiles = pygame.sprite.Group()  # 미사일들을 관리하는 Group 객체 missiles 생성

missiles.add(Missile(100, 100))  # 미사일 객체를 100, 100 좌표에 생성해서 missiles 그룹에 추가
missiles.add(Missile(100, 400))  # 같은 방식
missiles.add(Missile(100, 700))  # 같은 방식

user_plane = Airplane(400, 400)  # 사용자 비행기 객체 생성


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("yurim/background.png")


bg_length = 800
bg1 = Background(0, 0)
bg2 = Background(bg_length, 0)
bg3 = Background(0, 0)
bg4 = Background(0, 0)


def background_moving(drec_x, drec_y):

    bg1.x -= 5
    bg2.x -= 5

    if bg1.x == -bg_length:
        bg1.x = bg_length
    if bg2.x == -bg_length:
        bg2.x = bg_length

    screen.blit(bg1.image, (bg1.x, bg1.y))
    screen.blit(bg2.image, (bg2.x, bg2.y))
    pygame.display.update()


clock = pygame.time.Clock()  # clock (화면 리프레시 속도 조절용)
cnt = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 닫으면 나가기
            running = False
        if event.type == pygame.KEYDOWN:  # KEYDOWN 이벤트 발생
            if event.key == pygame.K_LEFT:  # left 를 눌렀다면
                direction = 'left'
                cnt += 1
            if event.key == pygame.K_RIGHT:  # right 를 눌렀다면
                direction = 'right'
                cnt += 1
        if event.type == pygame.KEYUP:  # 키보드에서 손가락을 떼면
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                cnt -= 1
    if cnt == 0 or cnt == 2:
        direction = 'forward'
    screen.fill((255, 255, 255))
    background_moving(user_plane.vel.x, user_plane.vel.y)

    for missile in missiles:  # missiles 그룹 내의 모든 missile 에 대해
        missile.update(user_plane.loc, user_plane.vel)  # 각 missile 객체의 update 함수 실행! 매개변수: 현재 비행기의 속도 벡터
        center_blit(missile)  # missile 의 현재 모습을 업데이트

    user_plane.update(direction)
    center_blit(user_plane)  # user_plane 의 현재 모습을 업데이트
    pygame.display.update()
    clock.tick(60)  # 화면 리프레시 속도 조절 (60 frames per second)
