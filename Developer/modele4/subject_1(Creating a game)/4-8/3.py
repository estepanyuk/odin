import pygame

WIDTH = 800
HEIGHT = 650
FPS = 30

# зададим цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (247, 146, 230)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    # def update(self, *args: Any, **kwargs: Any) -> None:
    def update(self):
        self.rect.x +=5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)

run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # обновление
    all_sprite.update()

    # рендеринг
    screen.fill(BLACK)
    all_sprite.draw(screen)

    # переворачиваем экран
    pygame.display.flip()

pygame.quit()














