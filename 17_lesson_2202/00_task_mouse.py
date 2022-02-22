import pygame as pg
from pygame.draw import circle, rect


FPS = 60
W = 700  # ширина экрана
H = 400  # высота экрана

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 100, 50)

sc = pg.display.set_mode((W, H))
clock = pg.time.Clock()

bomb = False  # летит ли бомба
x_goal = 0  # координаты цели
y_goal = 0
y_bomb = H  # координата бомбы

while 1:
    sc.fill(WHITE)
    pg.display.update()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        elif i.type == pg.MOUSEBUTTONDOWN:
            # если был клик, но другая бомба не летит
            if i.button == 1 and bomb == False:
                bomb = True
                x_goal = i.pos[0]
                y_goal = i.pos[1]
            # если бомба летит, но пока не достигла цели
    if bomb and y_bomb > y_goal:
        circle(sc, BLACK, (x_goal, y_bomb), 15)
        y_bomb -= 10
        pg.display.update()
        # если бомба уже достигла цели
    elif bomb and y_bomb <= y_goal:
        rect(sc, ORANGE, (x_goal - 25, y_bomb - 15, 50, 30))
        pg.display.update()
        pg.time.delay(1000)  # задержка, чтобы увидеть взрыв
        bomb = False
        y_bomb = H
    clock.tick(FPS)
