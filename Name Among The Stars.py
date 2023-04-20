# Get user's name and convert it to a list of characters
name = list(input("Please enter your name: "))

# Get the number of characters in the name
no_of_ch = len(name)

# Loop through each character in the name
for i in range(no_of_ch):
    # Loop through each character in the name again
    for j in range(no_of_ch):
        # Check if the two iterations match
        if i == j:
            # If they match, print the character
            print(name[i], end=" ")
        else:
            # If they don't match, print a *
            print("*", end=" ")
    # Move to the next row by printing an empty line
    print()
