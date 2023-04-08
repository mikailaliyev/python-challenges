# Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user-friendly format.

slices_total = int(input("how many slices of pizza did you have?\n"))
slices_consumed= int(input("how many slices of pizza did you eat?\n"))
print(f"You have {slices_total - slices_consumed} slices of pizza left")
