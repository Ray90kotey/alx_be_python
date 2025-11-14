# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in each row
    for i in range(size):
        print("*", end="")  # print without new line
    
    print()  # move to the next line after each row
    row += 1  # increment row counter
