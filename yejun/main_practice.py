import pygame
from yejun.missile import Missile

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles!")

missiles = pygame.sprite.Group()

missiles.add(Missile(400, 400))
missiles.add(Missile(100, 100))
missiles.add(Missile(700, 700))

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for missile in missiles:
        missile.update()
    screen.fill((0, 0, 0))
    for missile in missiles:
        screen.blit(missile.display_image, (missile.loc.x, missile.loc.y))
    pygame.display.update()
