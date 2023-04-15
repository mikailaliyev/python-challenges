# Create a simple maths quiz that will ask the user for their name 
# and then generate two random questions. 
# Store their name, the questions they were asked, their answers and their final score in a .csv file. 
# Whenever the program is run it should add to the .csv file and not overwrite anything
import random

user_name = input("What is your name?\n")
results ={}
results["name"] = user_name
math_ops = ["+", "-", "*"]
user_score = 0
for i in range(0, 2):
    question =  f"{random.randint(0 , 10)} {math_ops[random.randint(0, 2)]} {random.randint(0 , 10)}"
    user_answer = int(input(f"Quiz: {question}\n"))
    results[f"quiz#{i + 1}"] = str(question)
    results[f"answer#{i + 1}"] = str(user_answer)
    if user_answer == eval(question):
        user_score += 1
        print(f"Success!\nYour score is {user_score}")
    else:
        print("Failed!")
results["score"] = str(user_score)

print(results)

file = open("Quizzes.csv", "a")
file.write("name: " + ", " + results["name"] + "\n" 
           + "quiz#1:" + ", " + results["quiz#1"] + ", " + results["answer#1"] + '\n'
           + "quiz#2:" + ", " + results["quiz#2"] + ', ' + results["answer#2"] + '\n' 
           + "score:" + ", " + results["score"] + '\n')
file.close()

file = open("Quizzes.csv", "r")
print(file.read())
file.close()