import turtle
#turtle.speed(0)
turtle.pensize(5)
turtle.color("yellow","red")

turtle.begin_fill()
for i in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.goto(60,-150)
turtle.color("violet")
turtle.write("五角星",font=('Arial',20,'normal'))