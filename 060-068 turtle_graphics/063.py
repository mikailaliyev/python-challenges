# Draw three squares in a row with a gap between each. 
# Fill them using three different colours
import turtle

turtle.color("green","red")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(200)
turtle.pendown()

turtle.color("blue","white")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(200)
turtle.pendown()

turtle.color("black","blue")
turtle.begin_fill()
for i in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(200)
turtle.pendown()

turtle.exitonclick()