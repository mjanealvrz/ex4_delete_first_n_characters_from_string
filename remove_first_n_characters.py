# Write a program to remove characters from a string 
#starting from zero up to n and return a new string.

# Pseudocode

# Ask user to input song title
user = input("Input song title: ")

# Ask user the numbers to be removed
characters = int(input("How many characters to be removed? "))

# Create function to execute the removing of characters
def song(user, characters):
    # Return the new string
    return user[characters+1:]

# Call the function and store result
song_title = song(user, characters)

# Print the new song title
print("New Song Title:  ", song_title)