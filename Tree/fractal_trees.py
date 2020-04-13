import pygame
import random
from math import sin, cos, floor, pi

screenWidth = 800
screenHeight = 600
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Fractal Trees")

l = 200
angle = pi / 2
d_angle = pi / 4

PINK = (255,0,255)
WHITE = (255,255,255)

def frac(pos, angle, l) :
    if l < 1 :
        return

    #PINK = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    new_pos = (pos[0] + l * cos(angle), pos[1] - l * sin(angle))
    if l > 4 :
        pygame.draw.line(win, WHITE, (pos[0], pos[1]), (new_pos[0], new_pos[1]))
    else :
        pygame.draw.line(win, PINK, (pos[0], pos[1]), (new_pos[0], new_pos[1]))

    frac(new_pos, angle + d_angle, floor(l * 2 / 3))
    frac(new_pos, angle - d_angle, floor(l * 2 / 3))


run = True
while run :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] :
        d_angle -= pi / 180
    elif keys[pygame.K_RIGHT] :
        d_angle += pi / 180

    win.fill(0)

    frac((screenWidth // 2, screenHeight), angle, l)
    pygame.display.update()

pygame.quit()