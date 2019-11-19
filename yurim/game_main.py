import pygame


class background:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("background.jpg")


def move_background():
    global bg_length, bg1, bg2, screen

    bg1.y -= 2
    bg2.y -= 2

    if bg1.y == -bg_length:
        bg1.y = bg_length
    if bg2.y == -bg_length:
        bg2.y = bg_length

    screen.blit(bg1.image, (0, bg1.y))
    screen.blit(bg2.image, (0, bg2.y))
    pygame.display.update()


def runGame():
    global bg1, bg2, bg_length, clock

    # Set background
    bg_length = 600
    bg1 = background(0, 0)
    bg2 = background(bg_length, bg_length)

    # Event loop
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.K_SPACE:
                crashed = True

        move_background()



def initGame():
    global screen, airplane, clock

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Plane_Crash_Game.jpg')
    airplane = pygame.image.load("airplane.jpg")
    clock = pygame.time.Clock()
    runGame()


if __name__ == '__main__': initGame()