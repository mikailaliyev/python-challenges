# Display the following message:
# 1) Square
# 2) Triangle
# If the user enters 1, then it should ask them for the length of one of its sides and display the area. 
# If they select 2, it should ask for the base and height of the triangle and display the area. 
# If they type in anything else, it should give them a suitable error message.
import math

print("""1) Square
2) Triangle""")
user_input = int(input("Choose either first or second option by entering 1 or 2\n"))
if user_input == 1:
    square_side = int(input("Enter a side length for the square\n"))
    print(f"The square area is {square_side ** 2}")
elif user_input == 2:
    triangle_base = int(input("Enter the triangle base\n"))
    triangle_height = int(input("Enter the triangle height\n"))
    print(f"The triangle area is {0.5 * triangle_base * triangle_height}")
else:
    print("Error: you entered wrong number!")
