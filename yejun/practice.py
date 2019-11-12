import pygame
import math

pygame.init()
screen_w, screen_h = 800, 800
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Practice...!")
icon_image = pygame.image.load('ufo.png')
pygame.display.set_icon(icon_image)

my_image = pygame.image.load('ufo.png')
w = my_image.get_width()
h = my_image.get_height()
speed = 0.1
max_rot_speed = 0.2
X = pygame.math.Vector2(screen_w/2 - w/2, screen_h/2 - h/2)
M = pygame.math.Vector2()
v = pygame.math.Vector2(speed, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    M.x, M.y = pygame.mouse.get_pos()
    target_R, target_theta = (M - X).as_polar()
    v_R, v_theta = v.as_polar()
    print(target_R, target_theta, '|', target_R, target_theta)
    delta_theta = target_theta - v_theta
    rotated_image = pygame.transform.rotate(my_image, 0)
    screen.fill((0, 0, 0))
    screen.blit(rotated_image, (X.x, X.y))
    pygame.display.update()
