from turtle import *
import random as r


def generate_colors_list(count):
    colors = []
    alphabet = 'abcdef0123456789'
    for color in range(count):
        col = '#'
        for i in range(6):
            col += r.choice(alphabet)
        colors.append(col)
    return colors


def spiral(obj, col, angle):
    len = 5
    for i in range(150):
        obj.fd(len)
        obj.color(r.choice(col))
        obj.rt(angle)
        len += 3

t = Turtle()
t.speed(0)
colors = generate_colors_list(200)
spiral(t, colors, 30)
getscreen()
getcanvas().postscript(file='spiral1.eps')  # сохранить рисунок в виде файла

done()