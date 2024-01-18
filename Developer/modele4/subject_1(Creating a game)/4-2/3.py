import pygame

# инициализируем модуль
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 30

# зададим цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255,215,0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/ 2, HEIGHT /2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# создадим игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# цикл игры
run = True
while run:
    #держим цикл на парвильной скорости
    clock.tick(FPS)
    # событие
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # обновление
    all_sprites.update()

    # рендеринг
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()