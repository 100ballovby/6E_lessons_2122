import random as r
from turtle import *


def make_color_list(count):
    """
    Функция создает список случайных цветов в HEX-палитре
    :param count: количество цветов для генерации
    :return: list с цветами в HEX
    """
    colors = []  # в этом списке храню цвета
    alphabet = '0123456789abcdef'

    for col in range(count):  # повторить count раз
        color = '#'
        for symb in range(6):  # повторить 6 раз
            color += r.choice(alphabet)  # достаю случайную букву из алфавита
        colors.append(color)  # добавить цвет в список цветов

    return colors


def make_dot(obj, x, y, col, rad):
    """
    Функция рисует закрашенный круг в заданных координатах и определенного радиуса
    :param obj: черепашка
    :param x: координаты
    :param y: координаты
    :param col: цвет круга
    :param rad: радиус круга
    :return: None
    """
    obj.up()  # поднять перо
    obj.goto(x, y)  # перейти в х, у
    obj.color(col)  # устанавливаю цвет
    obj.down()  # опустить перо
    obj.dot(rad)  # рисую круг с радиусом rad

colors = make_color_list(1000)
t = Turtle()

for i in range(1000):
    c_x = r.randint(-400, 400)
    c_y = r.randint(-400, 400)
    color = r.choice(colors)
    radius = r.randint(10, 80)
    make_dot(t, c_x, c_y, color, radius)

done()

"""
Написать функцию, которая будет рисовать спирали из разных 
геометрических фигур. Спираль - это рисование обычной фигуры 
с постоянным увеличением длины стороны. 
Тип спирали задается градусом через аргумент функции. 
Каждая линий в спирали должна быть окрашена в случайный цвет 
"""
