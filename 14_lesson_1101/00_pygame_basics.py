import pygame as pg

# настроим окошко программы
screen = pg.display.set_mode((640, 480))  # размер окна программы 640x480 пикселей
clock = pg.time.Clock()  # отвечает за сменяемость кадров
finished = False  # флаг, который отвечает за работу игры


# если до начала игры нужно что-то отобразить
pg.display.update()  # обновляет экран игры

while not finished:  # пока игра не окончена
    clock.tick(30)  # задержка на количество кадров в секунду
    for event in pg.event.get():  # обрабатываю все события из списка событий
        if event.type == pg.QUIT:  # если событие = "ЗАКРЫТЬ ОКНО"
            finished = True  # True - закончено. Игра останавливается

    pg.display.update()  # обновляю экран внутри цикла программы
