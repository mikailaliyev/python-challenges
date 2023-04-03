# Ask for the total price of the bill, then ask how many diners there are. 
# Divide the total bill by the number of diners and show how much each person must pay.

total_price = float(input("What is the total price of the bill?\n"))
diners_count = float(input("How many diners are there?\n"))
bill_for_each_person = total_price / diners_count
print(f"Each person should pay {round(bill_for_each_person, 2)}")
