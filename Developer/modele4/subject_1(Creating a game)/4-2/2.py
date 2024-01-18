# импортировали модуль
import pygame

# инициализируем модуль
pygame.init()

WIDTH = 800
HEIGHT = 600

# настроли отрисоку окна
# screen = pygame.display.set_mode((1200, 800))
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# игровой цикл, пока пользователь не захотел выйти/закрыть окно
run = True
while run:
    #нажал ли пользователь кнопку закрыть окно/отслеживаем событие: 'закрытия окна'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # заполняем фон белым цветом
    screen.fill((255, 255, 255))

    # нарисовали синий в центре  радиусом 50
    pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2), 50)

    #рисуем красный квадрат
    red_square = pygame.Rect((50, 50), (100, 100))
    pygame.draw.rect(screen, (200, 0, 0), red_square, 60)

    # рисуем фиолетовый текст с кеглем/размером шрифта 50
    text_font = pygame.font.SysFont('Arial', 50)
    text_block = text_font.render('Hello, World! From Pygame', False, (102, 40, 184))
    screen.blit(text_block, (50, HEIGHT - 50))


    pygame.display.flip()
pygame.quit()

# решение 1 задачи от глеба латышева
import pygame
import sys
pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

r = pygame.Rect(550, 500, 100, 10)
pygame.draw.circle(screen, "red", (600, 400), 300)
pygame.draw.rect(screen, (255, 255, 0), r, 0)
pygame.draw.circle(screen, "yellow", (500, 300), 50)
pygame.draw.circle(screen, "black", (500, 300), 20)
pygame.draw.circle(screen, "white", (505, 305), 10)
pygame.draw.circle(screen, "yellow", (700, 300), 50)
pygame.draw.circle(screen, "black", (700, 300), 20)
pygame.draw.circle(screen, "white", (705, 305), 10)
pygame.draw.line(screen, "white", (505, 270), (560, 100), width=2)
pygame.draw.line(screen, "white", (705, 270), (760, 100), width=2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
