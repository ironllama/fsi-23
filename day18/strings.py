# Write a Python program to get a string made of the 
# first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return the string
# instead of an empty string.

source = "watermelon"
# target = source[:2] + source[8:]
target = source[:2] + source[-2:]  # Can also use negatives to get from end!
print("TARGET:", target)

# Write a Python program to get a single string from two 
# given strings, separated by a space and swap the first 
# two characters of each string.

one = "pine"
two = "apple"
onetwo = one + " " + two
swapped = onetwo[5] + onetwo[1:5] + onetwo[0] + onetwo[6:]
print("SWAPPED:", swapped)
