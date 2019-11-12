import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('ufo.png')
pygame.display.set_caption("Missiles!")
pygame.display.set_icon(icon)

player_image = pygame.image.load('ufo.png')
player_x = 370
player_y = 480
player_dx = 0
player_dy = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dx = -0.2
            elif event.key == pygame.K_RIGHT:
                player_dx = 0.2
            elif event.key == pygame.K_UP:
                player_dy = -0.2
            elif event.key == pygame.K_DOWN:
                player_dy = 0.2
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_dx = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                player_dy = 0
    screen.fill((0, 0, 0))
    player_x += player_dx
    player_y += player_dy
    player_x = player_x if player_x > 0 else 0
    player_x = player_x if player_x < 800 - 32 else 800 - 32
    player_y = player_y if player_y > 0 else 0
    player_y = player_y if player_y < 600 - 32 else 600 - 32

    screen.blit(player_image, (player_x, player_y))
    pygame.display.update()
