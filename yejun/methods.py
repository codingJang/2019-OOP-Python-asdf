import pygame
from yurim.button import *

__all__ = ['center_blit', 'center_rect', 'ask_replay']


def center_blit(screen, sprite):
    """
    어떤 sprite 의 display_image 를 loc 좌표를 중심으로 blit 한다
    :param sprite: 이 게임에서 사용하는 스프라이트 (airplane, missile, item, ... 단 background 예외)
    :return: None
    """
    screen.blit(sprite.display_image,
                (sprite.loc.x - sprite.display_image.get_width()/2,
                 sprite.loc.y - sprite.display_image.get_height()/2))


def center_rect(sprite):
    return sprite.display_image.get_rect().move(sprite.loc.x - sprite.width/2,
                                                sprite.loc.y - sprite.height/2)


def ask_replay(screen, options, bonus, user_plane):
    font = pygame.font.Font("Teko-Regular.ttf", 50)
    question1 = font.render('Do you want to replay?', 1, (0, 0, 0))
    question2 = font.render('If you have bonus point, you can continue!', 1, (0, 0, 0))
    # 게임 진행 여부 버튼
    replayButton = Button((0, 255, 0), 80, 450, 200, 80, 'Replay', 1)
    endButton = Button((0, 255, 0), 300, 450, 200, 80, 'End', 2)
    if bonus:
        continueButton = Button((0, 255, 0), 520, 450, 200, 80, 'continue', 3)
        options.add(continueButton)
    else:
        pygame.draw.rect(screen, (200, 200, 200), (520, 450, 200, 80), 0)
        text = font.render("continue", 1, (0, 0, 0))
        screen.blit(text, (520 + (100 - text.get_width() / 2), 450 + (40 - text.get_height() / 2)))

    screen.blit(question1, (240, 280))
    screen.blit(question2, (100, 350))
    options.add(replayButton, endButton)
    re = make_button(screen, options, plane=user_plane)
    return re
