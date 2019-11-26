"""
이유림이 반드시 참고해야 할 것...!!
****매우 중요****
대충 이런 flow 로 메인 코드가 개발되어야 협업이 편할 것 같음!
https://www.101computing.net/pygame-how-tos/
여기 이미지의 flow chart를 참고하시길
암튼 꼭 참고하세요
"""

import pygame  # pygame 가져오기
from yejun.missile import Missile  # 장예준이 만든 Missile 클래스
from junho.airplane import Airplane  # 장준호가 만든 Airplane 클래스
from yurim.background import Background  # 이유림이 만든 Background 클래스
from yejun.blit_methods import *


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles!")

missiles = pygame.sprite.Group()  # 미사일들을 관리하는 Group 객체 missiles 생성

missiles.add(Missile(100, 100))  # 미사일 객체를 100, 100 좌표에 생성해서 missiles 그룹에 추가
missiles.add(Missile(100, 400))  # 같은 방식
missiles.add(Missile(100, 700))  # 같은 방식

user_plane = Airplane(400, 400)  # 사용자 비행기 객체 생성

backgrounds = pygame.sprite.Group()

bg_length = 800
backgrounds.add(Background(0, 0))
backgrounds.add(Background(bg_length, 0))
backgrounds.add(Background(0, bg_length))
backgrounds.add(Background(bg_length, bg_length))

"""
def background_moving(dir_x, dir_y):

    for i in backgrounds:
        i.x -= dir_x*6
        i.y -= dir_y*6

    for i in backgrounds:
        if i.x < -bg_length:
            i.x = bg_length
        elif i.x > bg_length:
            i.x = -bg_length
        if i.y < -bg_length:
            i.y = bg_length
        elif i.y > bg_length:
            i.y = -bg_length

    for i in backgrounds:
        screen.blit(i.image, (i.x, i.y))

    # pygame.display.update() # 이 부분 틀렸음!!!!
"""

clock = pygame.time.Clock()  # clock (화면 리프레시 속도 조절용)
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:  # 닫으면 나가기
            running = False
    screen.fill((102, 204, 255))    # 배경 사이 틈 같은색으로 매꾸기
    # background_moving(user_plane.vel.x, user_plane.vel.y)

    # missile_collision = pygame.sprite.groupcollide(missiles, missiles, True, True)

    for background in backgrounds:
        background.moving(user_plane.vel)
        screen.blit(background.image, (background.x, background.y))

    missiles.update(screen, user_plane.loc, user_plane.vel)  # missiles Group 내의 모든 missile 에 대해 update() 함수 실행
    user_plane.update(screen, events)  # 같은 방식

    plane_collision = pygame.sprite.spritecollide(user_plane, missiles, True)
    if len(plane_collision) != 0:
        print("DEATH")

    pygame.display.update()
    clock.tick(60)  # 화면 리프레시 속도 조절 (60 frames per second)
