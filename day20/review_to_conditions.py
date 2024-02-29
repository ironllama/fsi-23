# 1. Ask your user for a first name value using the input function and
#     assign the result to a variable called first_name.
first_name = input("1a. Gimme a first name: ")

#    b. Ask your user for a last name value using the input function and
#        assign the result to a variable called last_name.
last_name = input("1b. Gimme a last name: ")

#    c. Combine first_name and last_name into a single variable full_name
#        and print out the length of the string contained in that variable.
# full_name = first_name + " " + last_name
full_name = f"{first_name} {last_name}"
print("1c:", full_name)


# 2. Ask your user for a greeting and store it in a variable called greeting.
greeting = input("2a. Gimme a greeting: ")

#    b. Ask your user for the number of times they want to repeat that
#        greeting and store it in a variable called count.
count = input("2b. How many times should I repeat the greeting? ")
count = int(count)

#    c. Print out whether or not the count is less than 100.
print("2c:", count < 100)

#    d. Print out the greeting repeated count number of times.
print("2d:", greeting * count)


# 3. Ask your user for the lowest value in a range and store it in a
#     variable called low.
low = int(input("3a. Lowest value for range: "))

#    b. Ask your user for the highest value in a range and store it in
#        a variable called high.
high = input("3b. Highest value in range: ")
high = int(high)

#    c. Ask the user for a value, and print whether or not that value
#        is in the range (inclusive).
new_value = input("3c. Enter a number: ")

if low <= int(new_value) <= high:
    print(f"3c. {new_value} is in the range between {low} and {high} (inclusive)!")
else:
    print(f"3c. {new_value} is outside the range.")
