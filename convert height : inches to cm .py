# Nested interactive loop
heights = []  # Empty list to store heights in inches

# Input loop
while True:
    try:
        # Prompt user for input
        x = float(input("Enter height in inches (or a negative number to stop): "))
        if x <= 0:
            break
        heights.append(x)  # Add valid height to the list
    except ValueError:
        print("Invalid input. Please enter a number.")

# Convert heights to centimeters using list comprehension
output = [x * 2.54 for x in heights]

# Print the converted heights
print("Heights in centimeters:", output)
