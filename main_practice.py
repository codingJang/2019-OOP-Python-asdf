# coding=utf-8
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
from yurim.button import Button


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles!")

backgrounds = pygame.sprite.Group()
bg_length = 800
backgrounds.add(Background(0, 0))
backgrounds.add(Background(bg_length, 0))
backgrounds.add(Background(0, bg_length))
backgrounds.add(Background(bg_length, bg_length))

missiles = pygame.sprite.Group()  # 미사일들을 관리하는 Group 객체 missiles 생성
missiles.add(Missile(100, 100))  # 미사일 객체를 100, 100 좌표에 생성해서 missiles 그룹에 추가
missiles.add(Missile(100, 250))  # 같은 방식
missiles.add(Missile(100, 400))  # 같은 방식
missiles.add(Missile(100, 550))  # 같은 방식
missiles.add(Missile(100, 700))  # 같은 방식

user_plane = Airplane(400, 400)  # 사용자 비행기 객체 생성

clock = pygame.time.Clock()  # clock (화면 리프레시 속도 조절용)
running = True
while running:
    events = pygame.event.get()  # 이벤트 모음
    for event in events:
        if event.type == pygame.QUIT:  # 닫으면 나가기
            running = False
    screen.fill((102, 204, 255))    # 배경 사이 틈 같은색으로 매꾸기

    backgrounds.update(screen, user_plane.vel) # backgrounds Group 내의 모든 background 에 대해 update() 함수 실행
    missiles.update(screen, user_plane.loc, user_plane.vel)  # missiles 에 대해 실행
    user_plane.update(screen, events)  # user_plane 의 업데이트 실행

    plane_missiles_collisions = pygame.sprite.spritecollide(user_plane, missiles, True,
                                                            collided=pygame.sprite.collide_mask)
    if len(plane_missiles_collisions) != 0:  # 여기가 비행기가 미사일과 충돌했는지 검출하는 부분!
        print("DEATH")

    missiles_collisions = pygame.sprite.groupcollide(missiles, missiles, False, False,
                                                     collided=pygame.sprite.collide_mask)
    for missile1 in missiles_collisions:
        for missile2 in missiles_collisions[missile1]:
            if missile1 is not missile2:
                missile1.kill()
                missile2.kill()

    pygame.display.update()
    clock.tick(60)  # 화면 리프레시 속도 조절 (60 frames per second)
