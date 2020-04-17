import pygame
from math import sin, cos, pi

NEON_GREEN = (57, 255, 20)

screenWidth = 1000
screenHeight = 800
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Fractal Triangles")

l = screenHeight
v1 = (screenWidth // 2, 50) 
v2 = (v1[0] + l * cos(pi / 3), v1[1] + l * sin(pi / 3))
v3 = (v1[0] - l * cos(pi / 3), v1[1] + l * sin(pi / 3))

lines = []

def frac(v1, v2, v3) :
    if abs(v1[0] - v2[0]) < 2:
        return

    lines.append((v1, v2, v3))

    v12 = ((v1[0] + v2[0]) // 2, (v1[1] + v2[1]) // 2)
    v13 = ((v1[0] + v3[0]) // 2, (v1[1] + v3[1]) // 2)
    v23 = ((v3[0] + v2[0]) // 2, (v3[1] + v2[1]) // 2)

    frac(v1, v12, v13)
    frac(v2, v12, v23)
    frac(v3, v13, v23)

frac(v1, v2, v3)

color = pygame.Color(255, 255, 255)

win.fill(0)
i = 0
run = True
play = False
while run :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] :
        play = True

    if play :
        line = lines[i]
        v1, v2, v3 = line[0], line[1], line[2]

        hue = 360 * i / len(lines)
        color.hsva = (hue, 100, 100, 100)

        pygame.draw.line(win, color, (v1[0], v1[1]), (v2[0], v2[1]))
        pygame.draw.line(win, color, (v2[0], v2[1]), (v3[0], v3[1]))
        pygame.draw.line(win, color, (v3[0], v3[1]), (v1[0], v1[1]))   

        pygame.display.update()
        i += 1

        if i == len(lines) :
            pygame.time.delay(1000)
            i = 0
            win.fill(0)

pygame.quit()