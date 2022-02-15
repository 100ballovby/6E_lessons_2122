import pygame as pg
from pygame.draw import rect, circle, polygon


def draw_house(surface, x, y, width, height):
    BEIGE = (240, 228, 175)
    ROUGE = (166, 73, 30)
    # рисую саму коробку дома
    rect(surface, BEIGE, [x, y, width, height])
    polygon(surface, ROUGE, [
        [x - (width / 10), y],
        [x + width + (width / 10), y],
        [x + (width // 2), y - 50]
    ])


W = 1280
H = 640
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

player_x = W // 2
player_y = H // 2

finished = False
while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

    screen.fill((0, 0, 0))

    house_x = 50
    house_y = 110

    for i in range(5):
        draw_house(screen, house_x, house_y, 50, 35)
        house_x += 80
        house_y += 50
    circle(screen, (0, 0, 255), [player_x, player_y], 40)

    keys = pg.key.get_pressed()  # проверяю, нажал ли кто-то на кнопку
    if keys[pg.K_a]:
        player_x -= 10
    if keys[pg.K_d]:
        player_x += 10

    pg.display.update()