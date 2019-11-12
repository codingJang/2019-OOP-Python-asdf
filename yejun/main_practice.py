"""
이유림이 반드시 참고해야 할 것...!!
****매우 중요****
대충 이런 flow 로 메인 코드가 개발되어야 협업이 편할 것 같음!
https://www.101computing.net/pygame-how-tos/
여기 이미지의 flow chart를 참고하시길
"""

import pygame  # pygame 가져오기
from yejun.missile import Missile  # 내가 만든 Missiles 클래스

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles!")

missiles = pygame.sprite.Group()  # 미사일들을 관리하는 Group 객체 missiles 생성

missiles.add(Missile(400, 400))  # 미사일 객체를 400, 400 좌표에 생성해서 missiles 그룹에 추가
missiles.add(Missile(100, 100))  # 같은 방식
missiles.add(Missile(700, 700))  # 같은 방식

running = True
clock = pygame.time.Clock()  # clock (화면 리프레시 속도 조절용)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 닫으면 나가기
            running = False
    screen.fill((0, 0, 0))
    for missile in missiles:  # missiles 그룹 내의 모든 missile 에 대해
        missile.update()  # 각 missile 객체의 update 함수 실행!
        screen.blit(missile.display_image, (missile.loc.x, missile.loc.y))  # missile 의 현재 모습을 업데이트
    pygame.display.update()
    clock.tick(60)  # 화면 리프레스 속도 조절 (60 frames per second)
