import pygame

pygame.init()
win = pygame.display.set_mode((500 + (4 * 4), 500 + (4 * 4)))
pygame.display.set_caption("Gemu")

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

score = 0


class bird(object):
    walkRight = [pygame.image.load(os.path.join('bird', 'br1.png')), pygame.image.load(os.path.join('bird', 'br2.png')),
                 pygame.image.load(os.path.join('bird', 'br3.png'))]

    walkLeft = [pygame.image.load(os.path.join('bird', 'bl1.png')), pygame.image.load(os.path.join('bird', 'bl2.png')),
                pygame.image.load(os.path.join('bird', 'bl3.png'))]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 7

    def render(self, win):
        self.move()
        if self.walkCount + 1 >= 9:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


class enemy(object):
    walkRight = [pygame.image.load(os.path.join('enemy', 'r1.png')), pygame.image.load(os.path.join('enemy', 'r2.png')),
                 pygame.image.load(os.path.join('enemy', 'r3.png')),
                 pygame.image.load(os.path.join('enemy', 'r4.png')), pygame.image.load(os.path.join('enemy', 'r5.png')),
                 pygame.image.load(os.path.join('enemy', 'r6.png')),
                 pygame.image.load(os.path.join('enemy', 'r7.png')), pygame.image.load(os.path.join('enemy', 'r8.png')),
                 pygame.image.load(os.path.join('enemy', 'r9.png')),
                 pygame.image.load(os.path.join('enemy', 'r10.png')),
                 pygame.image.load(os.path.join('enemy', 'r11.png')),
                 pygame.image.load(os.path.join('enemy', 'r12.png')),
                 pygame.image.load(os.path.join('enemy', 'r13.png')),
                 pygame.image.load(os.path.join('enemy', 'r14.png')),
                 pygame.image.load(os.path.join('enemy', 'r15.png')),
                 pygame.image.load(os.path.join('enemy', 'r16.png')),
                 pygame.image.load(os.path.join('enemy', 'r17.png')),
                 pygame.image.load(os.path.join('enemy', 'r18.png')), ]

    walkLeft = [pygame.image.load(os.path.join('enemy', 'l1.png')), pygame.image.load(os.path.join('enemy', 'l2.png')),
                pygame.image.load(os.path.join('enemy', 'l3.png')),
                pygame.image.load(os.path.join('enemy', 'l4.png')), pygame.image.load(os.path.join('enemy', 'l5.png')),
                pygame.image.load(os.path.join('enemy', 'l6.png')),
                pygame.image.load(os.path.join('enemy', 'l7.png')), pygame.image.load(os.path.join('enemy', 'l8.png')),
                pygame.image.load(os.path.join('enemy', 'l9.png')),
                pygame.image.load(os.path.join('enemy', 'l10.png')),
                pygame.image.load(os.path.join('enemy', 'l11.png')),
                pygame.image.load(os.path.join('enemy', 'l12.png')),
                pygame.image.load(os.path.join('enemy', 'l13.png')),
                pygame.image.load(os.path.join('enemy', 'l14.png')),
                pygame.image.load(os.path.join('enemy', 'l15.png')),
                pygame.image.load(os.path.join('enemy', 'l16.png')),
                pygame.image.load(os.path.join('enemy', 'l17.png')),
                pygame.image.load(os.path.join('enemy', 'l18.png')), ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 10
        self.visible = True

    def render(self, win):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 15, self.y, 28, 60)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('Hit')


walkright = [pygame.image.load(os.path.join('player', 'r1.png')), pygame.image.load(os.path.join('player', 'r2.png')),
             pygame.image.load(os.path.join('player', 'r3.png')),
             pygame.image.load(os.path.join('player', 'r4.png')), pygame.image.load(os.path.join('player', 'r5.png')),
             pygame.image.load(os.path.join('player', 'r6.png')),
             pygame.image.load(os.path.join('player', 'r7.png')), pygame.image.load(os.path.join('player', 'r8.png')),
             pygame.image.load(os.path.join('player', 'r9.png')),
             pygame.image.load(os.path.join('player', 'r10.png')), pygame.image.load(os.path.join('player', 'r11.png')),
             pygame.image.load(os.path.join('player', 'r12.png')),
             pygame.image.load(os.path.join('player', 'r13.png')), pygame.image.load(os.path.join('player', 'r14.png')),
             pygame.image.load(os.path.join('player', 'r15.png')),
             pygame.image.load(os.path.join('player', 'r16.png')), pygame.image.load(os.path.join('player', 'r17.png')),
             pygame.image.load(os.path.join('player', 'r18.png')), ]

walkleft = [pygame.image.load(os.path.join('player', 'l1.png')), pygame.image.load(os.path.join('player', 'l2.png')),
            pygame.image.load(os.path.join('player', 'l3.png')),
            pygame.image.load(os.path.join('player', 'l4.png')), pygame.image.load(os.path.join('player', 'l5.png')),
            pygame.image.load(os.path.join('player', 'l6.png')),
            pygame.image.load(os.path.join('player', 'l7.png')), pygame.image.load(os.path.join('player', 'l8.png')),
            pygame.image.load(os.path.join('player', 'l9.png')),
            pygame.image.load(os.path.join('player', 'l10.png')), pygame.image.load(os.path.join('player', 'l11.png')),
            pygame.image.load(os.path.join('player', 'l12.png')),
            pygame.image.load(os.path.join('player', 'l13.png')), pygame.image.load(os.path.join('player', 'l14.png')),
            pygame.image.load(os.path.join('player', 'l15.png')),
            pygame.image.load(os.path.join('player', 'l16.png')), pygame.image.load(os.path.join('player', 'l17.png')),
            pygame.image.load(os.path.join('player', 'l18.png')), ]

playerStandRight = pygame.image.load(os.path.join('player', 'r_idle.png'))
playerStandLeft = pygame.image.load(os.path.join('player', 'l_idle.png'))

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
hitbox = (x + 20, y, 28, 60)
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
    minotaur.render(win)
    flappy.render(win)
    hitbox = (x + 10, y, 40, 80)
    pygame.draw.rect(win, (255, 0, 0), hitbox, 2)
    t_score = font.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(t_score, (350, 10))
    t_shootCount = font.render("Shoot Count: " + str(shootCount), 1, (255, 255, 255))
    win.blit(t_shootCount, (10, 10))

    pygame.display.update()


def hit():
    font1 = pygame.font.SysFont('arial', 100)
    timer = font1.render('-5', 1, (255, 0, 0))
    win.blit(timer, (250 - (timer.get_width() / 2), 200))
    pygame.display.update()
    i = 0
    while i < 300:
        pygame.time.delay(10)
        i += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = 301
                pygame.quit()


font = pygame.font.SysFont("arial", 30, True, False)
minotaur = enemy(100, 436, 64, 64, 400)
flappy = bird(-100, 236, 64, 64, 600)
run = True
shootloop = 0
shootCount = 0
bullets = []
while run:
    clock.tick(30)
    hitbox = (x + 10, y, 40, 80)

    if hitbox[1] < minotaur.hitbox[1] + minotaur.hitbox[3] and hitbox[1] + hitbox[3] > minotaur.hitbox[1]:
        if hitbox[0] + hitbox[2] > minotaur.hitbox[0] and hitbox[0] < minotaur.hitbox[0] + minotaur.hitbox[2]:
            hit()
            x = 50
            y = 425
            isJump = False
            jumpCount = 10
            score -= 5

    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < minotaur.hitbox[1] + minotaur.hitbox[3] and bullet.y + bullet.radius > \
                minotaur.hitbox[1]:
            if bullet.x + bullet.radius > minotaur.hitbox[0] and bullet.x - bullet.radius < minotaur.hitbox[1] + \
                    minotaur.hitbox[3]:
                hitSound.play()
                minotaur.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

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
        bulletSound.play()
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 8:
            shootCount += 1
            bullets.append(fireball(round(x + width // 2), round(y + height // 2), 3, (0, 204, 225), facing))

    drawWindow()
pygame.quit()