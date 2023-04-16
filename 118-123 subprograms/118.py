# Define a subprogram that will ask the user to enter a number 
# and save it as the variable “num”. 
# Define another subprogram that will use “num” and count from 1 to that number

def user_num():
    num = int(input("Enter a number more than 1\n"))
    return num
    
def count():
    for i in range(1, user_num() + 1):
        print(i)

count()