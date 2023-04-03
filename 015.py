# Ask the user to enter their favourite colour. 
# If they enter “red”, “RED” or “Red” display the message “I like red too”, 
# otherwise display the message “I don’t like [colour], I prefer red”

user_favorite_color = input("Enter your favorite color\n")
if user_favorite_color == "red" or user_favorite_color == "RED" or user_favorite_color == "Red":
    print("I like red too")
else:
    print(f"I don’t like {user_favorite_color}, I prefer red")
