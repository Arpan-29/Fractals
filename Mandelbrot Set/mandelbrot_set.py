import pygame

f = 1

screenWidth = f * 800
screenHeight = f * 600
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Mandelbrot")

max_iter = 100
pxarray = pygame.PixelArray(win)

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
        for x in range(screenWidth // f) :
            for y in range(screenHeight // f) :

                a = 4 * x / (screenWidth // f) - 2
                b = 4 * y / (screenHeight // f) - 2

                ca = a
                cb = b

                n = 0
                while n < max_iter :
                    aa = a * a - b * b
                    bb = 2 * a * b

                    a = aa + ca
                    b = bb + cb

                    if abs(a + b) > 16 :
                        break

                    n += 1

                bright = 255 * n / max_iter
                if n == max_iter :
                    bright = 0

                # bright = 0
                # if n == max_iter :
                #     bright = 255

                pxarray[f * x, f * y] = (bright,bright,bright)
                pygame.display.update()

        play = False