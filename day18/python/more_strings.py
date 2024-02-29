# Create a variable called tongue_twister, assign your favorite tongue twister to that variable as a string.
tongue_twister = "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t fuzzy, was he?"

# Then, create a variable called count, assign a number between 2 and 1,000 to that variable.
count = 15

# Print out the uppercase version of that tongue twister repeated count number of times.
print(tongue_twister.upper() * count)

# Assign that repeated string to a new variable called tongue_twisters.
tongue_twisters = tongue_twister.upper() * count

# Print the lowercase version of that variable's (tongue_twisters) value.
print(tongue_twisters.lower())

# Then, print the result of multiplying the length of that variable's value by 15,000.
print(len(tongue_twisters) * 15000)

# Reassign the value of tongue_twister to be the string 'haha'.
tongue_twister = 'haha'

# Reassign the value of tongue_twisters to be the number 9000.
tongue_twisters = 9000

# Combine the two variables into a single string using an f-string
something = f"{tongue_twister}{tongue_twisters}"

# Print the result. (eg. 'haha9000')
print(something)

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

first_letter = tongue_twister[0]
rest_of_word = tongue_twister[1:].replace(first_letter, '$')
print(first_letter + rest_of_word)

# print(tongue_twister[0] + tongue_twister[1:].replace(tongue_twister[0], '$'))  # Same as one line. Cryptic?
