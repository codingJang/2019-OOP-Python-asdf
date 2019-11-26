import pygame


def center_blit(screen, sprite):
    """
    어떤 sprite 의 display_image 를 loc 좌표를 중심으로 blit 한다
    :param sprite: 이 게임에서 사용하는 스프라이트 (airplane, missile, item, ... 단 background 예외)
    :return: None
    """
    screen.blit(sprite.display_image,
                (sprite.loc.x - sprite.display_image.get_width()/2,
                 sprite.loc.y - sprite.display_image.get_height()/2))
