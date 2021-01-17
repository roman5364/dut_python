import os
import pygame

pygame.init()
win = pygame.display.set_mode((500 + (4 * 4), 500 + (4 * 4)))
pygame.display.set_caption("Gemu")

walkright = [pygame.image.load('r1.png'), pygame.image.load('r2.png'), pygame.image.load('r3.png'),
             pygame.image.load('r4.png'), pygame.image.load('r5.png'), pygame.image.load('r6.png'),
             pygame.image.load('r7.png'), pygame.image.load('r8.png'), pygame.image.load('r9.png'),
             pygame.image.load('r10.png'), pygame.image.load('r11.png'), pygame.image.load('r12.png'),
             pygame.image.load('r13.png'), pygame.image.load('r14.png'), pygame.image.load('r15.png'),
             pygame.image.load('r16.png'), pygame.image.load('r17.png'), pygame.image.load('r18.png'), ]

walkleft = [pygame.image.load('l1.png'), pygame.image.load('l2.png'), pygame.image.load('l3.png'),
            pygame.image.load('l4.png'), pygame.image.load('l5.png'), pygame.image.load('l6.png'),
            pygame.image.load('l7.png'), pygame.image.load('l8.png'), pygame.image.load('l9.png'),
            pygame.image.load('l10.png'), pygame.image.load('l11.png'), pygame.image.load('l12.png'),
            pygame.image.load('l13.png'), pygame.image.load('l14.png'), pygame.image.load('l15.png'),
            pygame.image.load('l16.png'), pygame.image.load('l17.png'), pygame.image.load('l18.png'), ]

playerStandRight = pygame.image.load('r_idle.png')
playerStandLeft = pygame.image.load('l_idle.png')

background = pygame.image.load("bg.png")

clock = pygame.time.Clock()

x = 50
y = 425
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0
lastMove = 'right'


class fireball(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def render(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    global animCount
    win.blit(background, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkleft[animCount // 5], (x, y))
        animCount += 1

    elif right:
        win.blit(walkright[animCount // 5], (x, y))
        animCount += 1

    elif lastMove == 'right':
        win.blit(playerStandRight, (x, y))

    elif lastMove == 'left':
        win.blit(playerStandLeft, (x, y))

    for bullet in bullets:
        bullet.render(win)

    pygame.display.update()


run = True
bullets = []
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] | keys[pygame.K_a] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] | keys[pygame.K_d] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        animCount = 0
    if not (isJump):
        # if keys[pygame.K_UP] | keys[pygame.K_w] and y > 5:
        #    y -= speed
        # if keys[pygame.K_DOWN] | keys[pygame.K_s] and y < 500 - height - 5:
        #    y += speed
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
    if keys[pygame.K_KP_ENTER]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 8:
            bullets.append(fireball(round(x + width // 2), round(y + height // 2), 3, (0, 204, 225), facing))

    drawWindow()
pygame.quit()