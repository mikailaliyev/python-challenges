# Create a list of six school subjects. 
# Ask the user which of these subjects they don’t like. 
# Delete the subject they have chosen from the list before you display the list again

school_subjects = ["Math", "Physics", "Astronomy", "Chemistry", "Literature", "English"]
print(school_subjects)
user_hate = input("Which of these school subject you don't like?\n")
school_subjects.remove(user_hate)
print(f"We removed it from the curicculum! Here a new list of subjects:\n{school_subjects} ")
