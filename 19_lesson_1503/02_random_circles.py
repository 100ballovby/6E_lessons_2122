from turtle import *
import random as r


t = Turtle()
t.shape('turtle')

colors = ['#eb4034', '#7189f5', '#ffe875', '#b375ff',
          '#ff758c', '#d1821b', '#76b37d', '#1f0d94']

for i in range(400):
    x = r.randint(-400, 400)
    y = r.randint(-400, 400)
    color = r.choice(colors)
    radius = r.randint(5, 100)

    t.up()
    t.goto(x, y)
    t.down()
    t.color(color)
    t.dot(radius)



done()
