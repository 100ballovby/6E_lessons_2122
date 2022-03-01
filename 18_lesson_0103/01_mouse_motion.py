import pygame as pg
from pygame.draw import rect, circle, polygon

W = 640
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

pg.mouse.set_visible(False)  # свойство отключает видимость курсора над экраном игры

finished = False
while not finished:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((255, 255, 255))
    if pg.mouse.get_focused():  # если мышь над экраном игры
        position = pg.mouse.get_pos()  # сохраняю координаты мыши в переменной
        circle(screen, (255, 0, 0), position, 20)  # рисую в тех же координатах шарик

    pg.display.update()