import pygame
import math

pygame.init()

my_image = pygame.image.load('ufo.png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Practice...!")
pygame.display.set_icon(my_image)

X = pygame.math.Vector2(384, 284)
angle = 0
delta = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta = 0.5
            if event.key == pygame.K_RIGHT:
                delta = -0.5
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                delta = 0
    angle += delta
    rotated_image = pygame.transform.rotate(my_image, angle)
    w = my_image.get_width()
    h = my_image.get_height()
    rw = rotated_image.get_width()
    rh = rotated_image.get_height()
    screen.fill((0, 0, 0))
    screen.blit(rotated_image, (X.x + w/2 - rw/2, X.y + h/2 - rh/2))
    pygame.display.update()