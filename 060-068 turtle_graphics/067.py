import turtle


for i in range(0, 10):
    turtle.right(36)
    for i in range(0, 8):
        turtle.right(45)
        turtle.forward(50)

turtle.hideturtle()
turtle.exitonclick()
