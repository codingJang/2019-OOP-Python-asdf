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
from yejun.missile import *  # 장예준이 만든 Missile 클래스
from junho.airplane import *  # 장준호가 만든 Airplane 클래스
from yurim.background import *  # 이유림이 만든 Background 클래스
from yejun.blit_methods import *
from yurim.button import *
from yurim.addmissile import *


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles!")


backgrounds = pygame.sprite.Group()
bg_length = 800
backgrounds.add(Background(0, 0), Background(bg_length, 0), Background(0, bg_length), Background(bg_length, bg_length))

options = pygame.sprite.Group()

# 시작 화면
chooseButton = Button((0, 223, 0), 220, 550, 360, 80, 'Choose your airplane!')
options.add(chooseButton)
make_button(screen, options, "yurim/startBackground.png")
options.remove(chooseButton)

# 비행기 옵션 선택
user_plane = None
option1 = Button((0, 255, 0), 80, 500, 200, 80, 'Option 1', 1)
option2 = Button((0, 255, 0), 300, 500, 200, 80, 'Option 2', 2)
option3 = Button((0, 255, 0), 520, 500, 200, 80, 'Option 3', 3)
startButton = Button((0, 255, 0), 80, 600, 200, 80, 'Game start', 1)
backButton = Button((0, 255, 0), 520, 600, 200, 80, 'Back', 2)

page = True
while page:
    options.add(option1, option2, option3)
    op = make_button(screen, options, "yurim/airplanebackground.png")
    if op:
        options.remove(option1, option2, option3)
        options.add(startButton, backButton)
        re = 2
        if op == 1:
            re = make_button(screen, options, "yurim/airplane.png")
            user_plane = Airplane(400, 400, 0)
        elif op == 2:
            re = make_button(screen, options, "yurim/Jetplane.png")
            user_plane = Jetplane(400, 400, 0)
        elif op == 3:
            re = make_button(screen, options, "yurim/stealth.png")
            user_plane = Jetplane(400, 400, 0)
        options.remove(startButton, backButton)
        if re == 1:
            page = False
        else:
            continue

missiles = pygame.sprite.Group()  # 미사일들을 관리하는 Group 객체 missiles 생성

clock = pygame.time.Clock()  # clock (화면 리프레시 속도 조절용)
start_time = pygame.time.get_ticks()    # 게임 시작 시간 저장

running = True
while running:
    time_since_enter = (pygame.time.get_ticks() - start_time)//1000  # 게임 시작 이후 진행 시간을 점수로 표시(초 단위)
    level = time_since_enter//10 + 1    # 레벨은 10초당 1레벨 증가로 지정
    events = pygame.event.get()  # 이벤트 모음
    for event in events:
        if event.type == pygame.QUIT:  # 닫으면 나가기
            running = False
    screen.fill((102, 204, 255))    # 배경 사이 틈 같은색으로 매꾸기

    backgrounds.update(screen, user_plane.vel)  # backgrounds Group 내의 모든 background 에 대해 update() 함수 실행

    add_missile(missiles, level)   # 게임 레벨에 따른 미사일 생성
    missiles.update(screen, user_plane.loc, user_plane.vel)  # missiles 에 대해 실행
    user_plane.update(screen, events)  # user_plane 의 업데이트 실행

    # 화면에 게임 레벨, 점수 표시
    font = pygame.font.Font("Teko-Regular.ttf", 40)
    level_text = font.render('Level ' + str(level), 1, (0, 0, 0))
    screen.blit(level_text, (10, 5))
    score_text = font.render('Score : ' + str(time_since_enter), 1, (0, 0, 0))
    screen.blit(score_text, (10, 40))

    plane_missiles_collisions = pygame.sprite.spritecollide(user_plane, missiles, True, collided=pygame.sprite.collide_mask)

    if len(plane_missiles_collisions) != 0:  # 여기가 비행기가 미사일과 충돌했는지 검출하는 부분!
        print("DEATH")

    missiles_collisions = pygame.sprite.groupcollide(missiles, missiles, False, False,
                                                     collided=pygame.sprite.collide_mask)
    for missile1 in missiles_collisions:  # 미사일 충돌 검출
        for missile2 in missiles_collisions[missile1]:
            if missile1 is not missile2:
                missile1.kill()
                missile2.kill()

    pygame.display.update()
    clock.tick(60)  # 화면 리프레시 속도 조절 (60 frames per second)
