# pattern_drawing.py
# This program draws a square pattern of asterisks using a while loop and nested for loop.

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while) for rows
while row < size:
    # Inner loop (for) for columns
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1

