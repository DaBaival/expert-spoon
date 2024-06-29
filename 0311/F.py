import turtle
#turtle.speed(0)
turtle.color("green","yellow")
turtle.fillcolor=turtle.color
turtle.begin_fill()
for i in range(0,12):
    turtle.seth(30*(i+1))
    turtle.circle(100,30)
    turtle.seth(-30+i*30)
    turtle.circle(100,30)
turtle.end_fill()
