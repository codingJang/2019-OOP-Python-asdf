import pygame
from yurim.button import *


def center_blit(screen, sprite):
    """
    어떤 sprite 의 display_image 를 loc 좌표를 중심으로 blit 한다
    :param sprite: 이 게임에서 사용하는 스프라이트 (airplane, missile, item, ... 단 background 예외)
    :return: None
    """
    screen.blit(sprite.display_image,
                (sprite.loc.x - sprite.display_image.get_width()/2,
                 sprite.loc.y - sprite.display_image.get_height()/2))


def ask_replay(screen, options):
    font = pygame.font.Font("Teko-Regular.ttf", 50)
    question = font.render('Do you want to replay?', 1, (0, 0, 0))
    # 게임 진행 여부 버튼
    replayButton = Button((0, 255, 0), 120, 400, 200, 80, 'Replay', 1)
    endButton = Button((0, 255, 0), 480, 400, 200, 80, 'End', 2)

    screen.blit(question, (240, 310))
    options.add(replayButton, endButton)
    re = make_button(screen, options)
    return re
