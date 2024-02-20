"""               Mini project
 1 - Print a welcome message to the user
 2 - Take a string (message) and a letter from the user
 3 - Count how many times this letter occurred
 4 - Calculate the percentage of the letter in the message
 5 - Print the output to the user
"""
# Welcome message
print("Welcome to our mini project!")
# Take the user inputs
user_message = input("Please enter your message! ")
user_letter = input("Please enter the letter ")

# count the occurrences
count = user_message.count(user_letter)
print(count)

# Calculate the percentage
len_message = len(user_message)
print(len_message)
percentage = count/len_message*100
print(percentage)

# Print the output to the user
print("The count of the letter", user_letter , "is", count)
print("The percentage of the letter", user_letter, "is", percentage)
