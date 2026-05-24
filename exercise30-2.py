from turtle import *
speed(10)
from random import randint
bgcolor('darkblue')
colors = ('red', 'yellow', 'green', 'orange', 'purple', 'white', 'magenta', 'pink', 'cyan', 'brown', 'gray', 'gold')
for i in range(100):
    color(colors[i % 12])
    up()
    goto(randint(-200, 200), randint(-200, 200))
    down()
    begin_fill()
    circle(randint(5, 50))
    end_fill()

done()