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
X = pygame.math.Vector2(screen_w/2 - w/2, screen_h/2 - h/2)
M = pygame.math.Vector2()
speed = 0.1
max_rot_speed = 0.2
v_direction = pygame.math.Vector2(1, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    M.x, M.y = pygame.mouse.get_pos()
    mouse_direction = (M - X).normalize()
    v_direction
    measured_angle = math.degrees(math.acos(mouse_direction.x))
    if direction.y > 0:
        measured_angle = - measured_angle
    delta = measured_angle - angle
    delta = delta if delta < ang_speed else ang_speed
    angle += delta
    rotated_image = pygame.transform.rotate(my_image, angle)
    direction.scale_to_length(trans_speed)
    X += direction
    screen.fill((0, 0, 0))
    screen.blit(rotated_image, (X.x, X.y))
    pygame.display.update()
