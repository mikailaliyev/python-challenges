# Draw a pattern that will change each time the program is run. 
# Use the random function to pick the number of lines, the length of each line 
# and the angle of each turn
import turtle, random
number_of_lines = random.randint(5, 10)


for i in range(0, number_of_lines):
    length_of_lines = random.randint(25, 100)
    angle_of_turns = random.randint(1, 365)
    turtle.right(angle_of_turns)
    turtle.forward(length_of_lines)

turtle.hideturtle()
turtle.exitonclick()
