# Draw an octagon that uses a different colour 
# (randomly selected from a list of six possible colours) for each line.
import turtle, random

colors = ["red", "green", "blue", "orange", "yellow", "white"]
turtle.Screen().bgcolor("black")
turtle.pensize(3)
turtle.hideturtle()

for i in range(0, 8):
    turtle.color(random.choice(colors))
    turtle.forward(100)
    turtle.right(45)
    
turtle.exitonclick()
