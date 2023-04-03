# Write a program that will ask for a number of days and then will show 
# how many hours, minutes and seconds are in that number of days.

number_of_days = int(input("Enter days\n"))
hours = number_of_days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"There are {hours} hours, {minutes} minutes and {seconds} seconds in {number_of_days} days")
