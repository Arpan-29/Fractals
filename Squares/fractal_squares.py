import pygame
from math import floor

screenWidth = 750
screenHeight = 750
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Fractal Triangles")

x = 0
y = 0
l = screenWidth

WHITE = (255,255,255)
BLACK = (0,0,0)
NEON = (70,102,255)

def frac(x, y, l) :
    if l < 2:
        return

    x += l / 3
    y += l / 3
    l /= 3

    x = floor(x)
    y = floor(y)
    l = floor(l)

    pygame.draw.rect(win, NEON, (x, y, l, l))
    pygame.display.update()

    frac(x - l, y - l, l)
    frac(x, y - l, l)
    frac(x + l, y - l, l)
    frac(x - l, y, l)
    frac(x + l, y, l)
    frac(x - l, y + l, l)
    frac(x, y + l, l)
    frac(x + l, y + l, l)

check = True
run = True
play = False
while run :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE] :
        play = True

    win.fill(WHITE)

    if play :
        if check :
            frac(x, y, l)
            pygame.display.update()
            check = False

pygame.quit()