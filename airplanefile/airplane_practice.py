import pygame
import math

pygame.init()

my_image = pygame.image.load("jet2.png")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Practice...!")
pygame.display.set_icon(my_image)

X = pygame.math.Vector2(384, 284)
angle = 0
delta = 0

clock = pygame.time.Clock()
cnt = 0

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # 1
                delta = 3
                cnt += 1
            if event.key == pygame.K_RIGHT:
                # -1
                delta = -3
                cnt += 1
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                cnt -= 1
    if cnt == 0:
        delta = 0
    angle += delta
    rotated_image = pygame.transform.rotate(my_image, angle)
    w = my_image.get_width()
    h = my_image.get_height()
    rw = rotated_image.get_width()
    rh = rotated_image.get_height()
    screen.fill((0, 255, 255))
    screen.blit(rotated_image, (X.x + w/2 - rw/2, X.y + h/2 - rh/2))
    pygame.display.update()
