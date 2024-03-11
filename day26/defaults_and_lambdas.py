# 1. Convert the following function to a lambda expression and assign it to
#     a variable called exp.
def exponentiate(base, exponent):
	return base ** exponent

exp = lambda base, exponent: base ** exponent


# 2. Print the function you created using a lambda expression in previous
#     exercise. What is the name of the function that was created?
print("2:", exp)


# 3. Create a lambda function that adds 15 to a given number passed in
#     as an argument.
lambda num: 15 + num


# 4. Create a lambda function that multiplies argument x with argument y
#     and print the result.
lambda x, y: x * y
