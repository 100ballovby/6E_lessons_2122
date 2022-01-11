import pygame as pg
from pygame.draw import rect, circle

screen = pg.display.set_mode((640, 480))
pg.display.set_caption('Моя первая игра на PyGame')
clock = pg.time.Clock()
finished = False

# нарисуем прямоугольник
rect(screen, (209, 153, 255), [100, 200, 320, 135])
rect(screen, (255, 255, 255), [310, 120, 100, 212], 5)
# где_рисуем, (цвет в RGB), [x, y, ширина, высота], толщина_линии
pg.display.update()

while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    pg.display.update()
