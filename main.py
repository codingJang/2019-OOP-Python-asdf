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
from yurim.button import *
from yurim.items import *

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles!")

backgrounds = pygame.sprite.Group()
bg_length = 800
backgrounds.add(Background(0, 0), Background(bg_length, 0),
                Background(0, bg_length), Background(bg_length, bg_length))

options = pygame.sprite.Group()
items = pygame.sprite.Group()

# 시작 화면
chooseButton = Button((0, 223, 0), 220, 550, 360, 80, 'Choose your airplane!')
options.add(chooseButton)
make_button(screen, options, "images/startBackground.png")
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
    op = make_button(screen, options, "images/airplanebackground.png")
    if op:
        options.remove(option1, option2, option3)
        options.add(startButton, backButton)
        re = 2
        if op == 1:
            re = make_button(screen, options, "images/airplanetext.png")
            user_plane = Airplane(400, 400, -90)
        elif op == 2:
            re = make_button(screen, options, "images/Jetplanetext.png")
            user_plane = Jetplane(400, 400, -90)
        elif op == 3:
            re = make_button(screen, options, "images/stealthtext.png")
            user_plane = Spaceship(400, 400, -90)
        options.remove(startButton, backButton)
        if re == 1:
            page = False
        else:
            continue

missiles = pygame.sprite.Group()  # 미사일들을 관리하는 Group 객체 missiles 생성

clock = pygame.time.Clock()  # clock (화면 리프레시 속도 조절용)
start_time = pygame.time.get_ticks()    # 게임 시작 시간 저장

running = True
bonus = 5
level = 1
while running:
    events = pygame.event.get()  # 이벤트 모음
    for event in events:
        if event.type == pygame.QUIT:  # 닫으면 나가기
            running = False
    screen.fill((102, 204, 255))    # 배경 사이 틈 같은색으로 매꾸기

    time_since_enter = (pygame.time.get_ticks() - start_time) // 1000 + bonus  # 게임 시작 이후 진행 시간을 점수로 표시(초 단위)

    delta_level = time_since_enter // 10 + 1 - level
    level = time_since_enter // 10 + 1  # 레벨은 10초당 1레벨 증가로 지정

    add_missile(missiles, level, user_plane.loc)  # 게임 레벨에 따른 미사일 생성
    make_items(items, time_since_enter)  # 아이템 생성

    backgrounds.update(screen, user_plane.vel)  # backgrounds Group 내의 모든 background 에 대해 update() 함수 실행
    user_plane.update(screen)  # user_plane 의 업데이트 실행
    items.update(screen, user_plane.vel)  # items 에 대해 실행
    missiles.update(screen, user_plane.loc, user_plane.vel)  # missiles 에 대해 실행

    # 화면에 게임 레벨, 점수 표시
    font = pygame.font.Font("Teko-Regular.ttf", 40)
    level_text = font.render('Level ' + str(level), 1, (0, 0, 0))
    screen.blit(level_text, (10, 5))
    score_text = font.render('Score : ' + str(time_since_enter), 1, (0, 0, 0))
    screen.blit(score_text, (10, 40))
    bonus_text = font.render('bonus : ' + str(bonus), 1, (0, 0, 0))
    screen.blit(bonus_text, (680, 5))

    # 비행기 - 아이템 충돌 검출
    plane_items_collisions = pygame.sprite.spritecollide(user_plane, items, True,
                                                         collided=pygame.sprite.collide_mask)
    bonus += len(plane_items_collisions)

    # 비행기 - 미사일 충돌 검출
    plane_missiles_collisions = pygame.sprite.spritecollide(user_plane, missiles, True,
                                                            collided=pygame.sprite.collide_mask)
    if len(plane_missiles_collisions) != 0:  # 비행기와 미사일이 충돌했다면
        font = pygame.font.Font("Teko-Regular.ttf", 50)
        question1 = font.render('Do you want to replay?', 1, (0, 0, 0))
        question2 = font.render('If you have more than five bonus, you can continue!', 1, (0, 0, 0))
        # 게임 진행 여부 버튼
        replayButton = Button((0, 255, 0), 80, 450, 200, 80, 'Replay', 1)
        endButton = Button((0, 255, 0), 300, 450, 200, 80, 'End', 2)
        options.add(replayButton, endButton)
        continueButton = Button((0, 255, 0), 520, 450, 200, 80, 'continue', 3)
        if bonus >= 5:
            options.add(continueButton)
        else:
            pygame.draw.rect(screen, (200, 200, 200), (520, 450, 200, 80), 0)
            text = font.render("continue", 1, (0, 0, 0))
            screen.blit(text, (520 + (100 - text.get_width() / 2), 450 + (40 - text.get_height() / 2)))
        screen.blit(question1, (240, 280))
        screen.blit(question2, (30, 350))
        re = make_button(screen, options)
        if continueButton in options:
            options.remove(continueButton)
        if re == 1:
            missiles.empty()
            items.empty()
            user_plane.set_initial(400, 400, -90)
            start_time = pygame.time.get_ticks()  # 게임 시작 시간 저장
            bonus = 0
        if re == 2:
            running = False
        if re == 3:
            bonus -= 5
            pass

    # 미사일 간 충돌 검출
    missiles_collisions = pygame.sprite.groupcollide(missiles, missiles, False, False,
                                                     collided=pygame.sprite.collide_mask)
    for missile1 in missiles_collisions:
        for missile2 in missiles_collisions[missile1]:
            if missile1 is not missile2:
                missile1.kill()
                missile2.kill()
                bonus += 1

    pygame.display.update()
    clock.tick(60)  # 화면 리프레시 속도 조절 (60 frames per second)
