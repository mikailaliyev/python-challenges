# Using the song “10 green bottles”, display the lines 
# “There are [num] green bottles hanging on the wall, 
# [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. 
# Then ask the question “how many green bottles will be hanging on the wall?” 
# If the user answers correctly, display the message 
# “There will be [num] green bottles hanging on the wall”. 
# If they answer incorrectly, display the message “No, try again” until they get it right. 
# When the number of green bottles gets down to 0, 
# display the message “There are no more green bottles hanging on the wall”

bottle_count = 2


while bottle_count > 0:
    print(f"""There are {bottle_count} green bottles hanging on the wall, 
{bottle_count} green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. 
""")
    bottle_count -= 1
    user_reply = int(input("How many green bottles will be hanging on the wall?\n"))
    if user_reply == bottle_count:
        print(f"There will be {bottle_count} green bottles hanging on the wall")        
    else:
        while user_reply != bottle_count:
            user_reply = int(input("No, try again\n"))

print("There are no more green bottles hanging on the wall")
