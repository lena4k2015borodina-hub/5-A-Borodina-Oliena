from turtle import*
speed(8)
color('blue')
for i in range(1,100,2):
  up()
  goto(i*2,i*2)
  down()
  circle(i)