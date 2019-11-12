import pygame


def move_background():
    global bg1_x, bg2_x, bg1_y, bg2_y, bg_length, bg1, bg2, screen

    bg1_x -= 2
    bg2_x -= 2

    if bg1_x == -bg_length:
        bg1_x = bg_length

    if bg2_x == -bg_length:
        bg2_x = bg_length

    screen.blit(bg1, (bg1_x, 0))
    screen.blit(bg2, (bg2_x, 0))

    pygame.display.update()


def runGame():
    global bg1, bg2, bg1_x, bg2_x, bg1_y, bg2_y, bg_length, clock

    # Set background
    bg_length = 600
    bg1_x = 0
    bg2_x = bg_length
    bg1_y = 0
    bg2_y = bg_length

    # Event loop
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:    # 키보드를 누른 후 뗄 때
                if event.key == pygame.K_UP:
                    pass

                elif event.key == pygame.K_DOWN:
                    pass

            if event.type == pygame.KEYUP:  # 키보드를 누를 때
                while event.key == pygame.K_UP:
                    move_background()

        # screen.blit(background, (0, 0))
        # pygame.display.flip()


def initGame():
    global screen, airplane, clock, bg1, bg2

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Plane_Crash_Game.jpg')
    airplane = pygame.image.load("airplane.jpg")
    bg1 = pygame.image.load("background.jpg")
    bg2 = bg1.copy()

    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__': initGame()