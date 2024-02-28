# Variables population and land_area refer to floats.
population = 2_000_000.0
land_area = 2500.0

# 1. Write an if statement that will print the population 
#    if it is less than 10,000,000.

if population < 10_000_000:
    print("Population:", population)

# 2. Write an if statement that will print the population 
#    if it is between 10,000,000 and 35,000,000.
population = 20_000_000.0
if 10_000_000 < population < 35_000_000:
    print("Population:", population)

# 3. Write an if statement that will print “Densely populated” 
#    if the land density (number of people per unit of area) is 
#    greater than 100.
if (population / land_area) > 100:
    print("Densely populated.")

# 4. Write an if statement that will print “Densely populated” 
#    if the land density (number of people per unit of area) 
#    is greater than 100, and “Sparsely populated” otherwise.
land_area = 250000.0
if (population / land_area) > 100:
    print("Densely populated.")
else:
    print("Sparsely populated.")

# 5. Write a Python program to add 'ing' at the end of a given 
#    string (length should be at least 3). If the given string 
#    already ends with 'ing' then add 'ly' instead. If the string 
#    length of the given string is less than 3, leave it unchanged.

# message = "Exercising"
message = "Fly"

if len(message) >= 3:
    if message[-3:] == 'ing':
        message += 'ly'
    else:
        message += 'ing'

print("MESSAGE:", message)
