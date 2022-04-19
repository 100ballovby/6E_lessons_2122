from turtle import *
import random as r


t = Turtle()
screen = Screen()  # создать экран
screen.bgcolor('#e3af90')  # выставить цвет фона
# screen.bgpic('путь_к_картинке')  чтобы поставить картинку на фон
colormode(255)  # чтобы работал RGB
red = 0
green = r.randint(0, 255)
blue = r.randint(0, 255)

x = 0
t.speed(0)
while x < 256:
    t.fd(50 + x)
    t.lt(163)
    t.color(red, green, blue)
    red += 1
    x += 1

done()
