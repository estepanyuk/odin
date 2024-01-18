# Задача 1
#Импортируем и инициализируем библиотеку
import pygame

pygame.init()

# Устанавливаем ширину и высоту окна в пикселях
WIDTH = 800
HEIGHT = 600

# Настраиваем окно отрисовки
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Игровой цикл выполняется, пока пользователь не захочет выйти
running = True
while running:

    # Нажал ли пользователь кнопку зыкрытия окна?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполняем фон белым цветом
    screen.fill((255, 255, 255))

    # Рисуем синий круг в центре экрана радиусом 50
    pygame.draw.circle(screen, (0, 0, 255), (WIDTH // 2, HEIGHT // 2), 50)

    # Рисуем красный контурный квадрат в верхнем левом углу экрана
    red_square = pygame.Rect((50, 50), (100, 100))
    pygame.draw.rect(screen, (200, 0, 0), red_square, 1)

    # Рисуем оранжевый текст с кеглем 60
    text_font = pygame.font.SysFont("any_font", 60)
    text_block = text_font.render(
        "Hello, World! From Pygame", False, (200, 100, 0)
    )
    screen.blit(text_block, (50, HEIGHT - 50))

	# Обновляем экран
    pygame.display.flip()

# Цикл завершился! Уходим.
pygame.quit()

# # задача 2
import pygame
import random

WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()


# задача 3
# # Импорт всех классов
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.boxlayout import BoxLayout
#
# from kivy.core.window import Window
#
# # Глобальные настройки
# Window.size = (250, 200)
# Window.clearcolor = (255 / 255, 186 / 255, 3 / 255, 1)
# Window.title = "Конвертер"
#
#
# class MyApp(App):
#
#     # Создание всех виджетов (объектов)
#     def __init__(self):
#         super().__init__()
#         self.label = Label(text='Конвертер')
#         self.miles = Label(text='Мили')
#         self.metres = Label(text='Метры')
#         self.santimetres = Label(text='Сантиметры')
#         self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
#         self.input_data.bind(text=self.on_text)  # Добавляем обработчик события
#
#     # Получаем данные и производит их конвертацию
#     def on_text(self, *args):
#         data = self.input_data.text
#         if data.isnumeric():
#             self.miles.text = 'Мили: ' + str(float(data) * 0.62)
#             self.metres.text = 'Метры: ' + str(float(data) * 1000)
#             self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100000)
#         else:
#             self.input_data.text = ''
#
#     # Основной метод для построения программы
#     def build(self):
#         # Все объекты будем помещать в один общий слой
#         box = BoxLayout(orientation='vertical')
#         box.add_widget(self.label)
#         box.add_widget(self.input_data)
#         box.add_widget(self.miles)
#         box.add_widget(self.metres)
#         box.add_widget(self.santimetres)
#
#         return box
#
#
# # Запуск проекта
# if __name__ == "__main__":
#     MyApp().run()
#задача 3
# Pygame шаблон - скелет для нового проекта Pygame
# import pygame
# import time
# import random
#
# pygame.init()
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
# dis_width = 800
# dis_height = 600
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Змейка от Skillbox')
# clock = pygame.time.Clock()
# snake_block = 10
# snake_speed = 15
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
#
#
# def Your_score(score):
#     value = score_font.render("Ваш счёт: " + str(score), True, yellow)
#     dis.blit(value, [0, 0])
#
#
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
#
#
# def gameLoop():
#     game_over = False
#     game_close = False
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#     x1_change = 0
#     y1_change = 0
#     snake_List = []
#     Length_of_snake = 1
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#     while not game_over:
#         while game_close == True:
#             dis.fill(blue)
#             message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
#             Your_score(Length_of_snake - 1)
#             pygame.display.update()
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
#         our_snake(snake_block, snake_List)
#         Your_score(Length_of_snake - 1)
#         pygame.display.update()
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
#         clock.tick(snake_speed)
#     pygame.quit()
#     quit()
#
#
# gameLoop()

# Pygame шаблон - скелет для нового проекта Pygame