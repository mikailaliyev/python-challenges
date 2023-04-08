# Update program 027 so that it will display the answer to two decimal places.

user_number = float(input("Enter a float point number with lots of decimal places\n"))
multiplied = user_number * 2
print(round(multiplied, 2))
