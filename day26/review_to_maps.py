# 1. Write a function to find the sum of the series, up to n terms.
#     ie. 2 + 22 + 222 + 2222 + .. n terms
#     Call the function with number_of_terms to verify that your
#     function works as expected.
number_of_terms = 5  # => 24690 (total of 2 + 22 + 222 + 2222 + 22222)

def add_terms(num_terms):
    total = 0
    digit = "2"

    for num in range(1, num_terms + 1):
        total += int(digit * num)  # 'digit * num' is repeating the digit

    return total

print("1:", add_terms(number_of_terms))

#    b. Change number_of_terms to verify that your function is correct.
number_of_terms = 3
print("1b:", add_terms(number_of_terms))
number_of_terms = 7
print("1b:", add_terms(number_of_terms))
number_of_terms = 9 
print("1b:", add_terms(number_of_terms))
number_of_terms = 10
print("1b:", add_terms(number_of_terms))


# 2. Print out the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# size = 1
# forward = True
# while not(size == 0 and not forward):
#     print("2:", " ".join(["*"] * size))

#     if forward:
#         size += 1
#     else:
#         size -= 1

#     if size == 5:
#         forward = False

for size in range(1, 6):
    print("2:", " ".join(["*"] * size))
for size in range(4, 0, -1):
    print("2:", " ".join(["*"] * size))


# 3. Write a function calculation() such that it can accept two variables
#     and calculate the addition and subtraction of them. It must return
#     both addition and subtraction results in a single function call.
def calculation(x, y):
    add_res = x + y
    sub_res = x - y
    return add_res, sub_res

print("3:", calculation(10, 6))


# 4. Generate a Python list of all the even numbers between 4 and 30
print("4:", list(range(2, 41, 2)))


# 5. Write a function that returns the largest item from the following list:
lst = [4, 6, 8, 24, 12, 2]
# def largest(in_lst):
#     return max(in_lst)

largest = lambda x: max(x)

print("5:", largest(lst))

#    b. Change the list to verify your function is correct.
lst = [46, 23, 67499, 23, 1]
print("5b:", largest(lst))


# 6. Write a function that given a string of odd length greater than 7,
#     it returns a new string made up of the middle three characters of
#     the string.
def middle_three(in_str):
    mid_pos = len(in_str) // 2
    return in_str[mid_pos - 1: mid_pos + 2]

print("6:", middle_three("extravaganzaa"))


# 7. Write a function that given two strings, s1 and s2, it returns a new
#     string with s2 in the middle of s1. If s1 has an odd number of
#     characters, bias s2 towards the left.
def put_in_middle(s1, s2):
    mid_pos = len(s1) // 2
    return s1[:mid_pos] + s2 + s1[mid_pos:]

print("7:", put_in_middle("watermelon", "sugar"))
