import pygame
import math

pygame.init()
screen_w, screen_h = 800, 800
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Practice...!")
icon_image = pygame.image.load('../images/ufo.png')
pygame.display.set_icon(icon_image)

my_image = pygame.image.load('../images/ufo.png')
w = my_image.get_width()
h = my_image.get_height()
speed = 0.2
max_rot_speed = 0.2
X = pygame.math.Vector2(screen_w/2, screen_h/2)
M = pygame.math.Vector2()
v = pygame.math.Vector2(speed, 0)
t = pygame.math.Vector2()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    M.update(pygame.mouse.get_pos())
    t.update(M - X)
    crossed = v.cross(t)
    _, v_theta = v.as_polar()
    if crossed > 0:
        v = v.rotate(max_rot_speed)
    else:
        v = v.rotate(-max_rot_speed)
    # print(v_R, v_theta)
    rotated_image = pygame.transform.rotate(my_image, -v_theta)
    rw = rotated_image.get_width()
    rh = rotated_image.get_height()
    X += v
    screen.fill((0, 0, 0))
    screen.blit(rotated_image, (X.x - rw/2, X.y - rh/2))
    pygame.display.update()
