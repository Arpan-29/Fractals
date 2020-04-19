import pygame

screenWidth = 512
screenHeight = 512
win = pygame.display.set_mode((screenWidth, screenHeight))

WHITE = (255,255,255)

def hilbert(i) :
    points = [[0, 0], [0, 1], [1, 1], [1, 0]]

    index = i & 3
    pt = points[index]

    for j in range(1, order) :
        i >>= 2
        index = i & 3

        l = 2 ** j

        if index == 0 :
            pt[0], pt[1] = pt[1], pt[0]
        elif index == 1 :
            pt[1] += l
        elif index == 2 :
            pt[0] += l
            pt[1] += l
        elif index == 3 :
            pt[0], pt[1] = l - 1 - pt[1], l - 1 - pt[0]
            pt[0] += l

    return pt 

def make_path() :
    path = []
    for i in range(total) :
        path.append(hilbert(i))

    return path

order = 4
N = 2 ** order
total = N ** 2
w = screenWidth // N

path = make_path()

color = pygame.Color(0, 0, 0) 
win.fill(0)

i = 1
frame = 0
run = True
play = False
while run :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] :
        play = True

    if play :
        x1 = w * path[i][0] + w // 2
        y1 = w * path[i][1] + w // 2
        x2 = w * path[i - 1][0] + w // 2
        y2 = w * path[i - 1][1] + w // 2
        
        hue = int(360 * i / total)  
        color.hsva = (hue, 100, 100, 100)
        pygame.draw.line(win, color, (x1, y1), (x2, y2), 2)

        i += 1
        if frame % 1 == 0 :
            pygame.display.update()
        
        pygame.time.delay(10)

        if i == total :
            pygame.time.delay(1000)
            win.fill(0)
            i = 1
            frame = 0 

        frame += 1

pygame.quit()