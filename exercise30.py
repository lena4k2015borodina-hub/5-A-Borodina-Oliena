from turtle import *
from random import randint

bgcolor('darkblue')

colors = ('red', 'yellow', 'green', 'orange', 'purple', 'white', 'magenta')
for i in range(1, 100):
    color(colors[i % 7])
    up()
    goto(randint(-200, 200), randint(-200, 200))
    down()
    dot(randint(1, 8))

done()