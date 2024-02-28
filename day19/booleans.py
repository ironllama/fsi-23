# What value does each expression produce? Verify your answers by print out
# the expressions with Python. Or, use the Python IDLE.

# True and not False # what is the output?
print(True and not False)

# True and not false # what is the output?
# print(True and not false)  # ERROR! Remember to use uppercase first letter for booleans.

false = True  # Kinda evil, don't do this.  This is a cautionary example.
print(True and not false)

# True or True and False # what is the output? # what is the output?
print(True or True and False)
# print(True or False)  # After evaluating the higher precedent 'and', looks like this.

# print(True or (True and False))  # Better! Use parenthesis from the beginning!

# not True or not False
print(True or not False)

# True and not 0 # what is the output?
print(True and not 0)  # Don't use numbers to mean booleans, if you can avoid it!
