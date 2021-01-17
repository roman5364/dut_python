import pygame
from pygame.locals import *
# install first from the lick https://www.pygame.org/download.shtml

pygame.init()
win = pygame.display.set_mode((500 + (4 * 4), 500 + (4 * 4)))
pygame.display.set_caption("Gemu")

x = 50
y = 50
width = 4 * 4
height = 60
speed = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(57)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] | keys[pygame.K_a] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] | keys[pygame.K_d] and x < 500 - width - 5:
        x += speed
    if not (isJump):
        if keys[pygame.K_UP] | keys[pygame.K_w] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] | keys[pygame.K_s] and y < 500 - height - 5:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 204, 225), (x, y, width, height))
    pygame.display.update()

pygame.quit()