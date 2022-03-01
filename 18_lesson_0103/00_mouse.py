import pygame as pg
from pygame.draw import rect, circle, polygon
from random import randint

WHITE = (255, 255, 255)
ORANGE = (252, 186, 3)
MINT = (48, 209, 155)
BLUE = (46, 196, 255)

W = 640
H = 640
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

e_x = W // 2
e_y = H // 2
go = False

p_x = 100
p_y = 200

finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True
        if event.type == pg.MOUSEBUTTONDOWN:  # если нажата кнопка мыши
            print(event.button, event.pos)  # написать ее номер и координаты
            if event.button == 1:
                circle(screen, (255, 255, 255), event.pos, 40)
            if enemy.collidepoint(event.pos):  # если мышь коснулась enemy
                go = True
        if event.type == pg.MOUSEMOTION:  # если мышь двигается
            print(event.pos)  # печатать ее координаты
            if player.collidepoint(event.pos):
                p_x = randint(0, W)
                p_y = randint(0, H)

    screen.fill(WHITE)
    enemy = rect(screen, ORANGE, [e_x, e_y, 50, 50])
    player = rect(screen, MINT, [p_x, p_y, 70, 70])

    # рисуем тут
    pg.display.update()

    if go:  # если go == True
        go = False
        e_x = randint(0, W)
        e_y = randint(0, H)