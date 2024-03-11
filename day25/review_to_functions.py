# 1. Ask the user for a number. Depending on whether the number is even or
#     odd, print out an appropriate message to the user. If the number is a
#     multiple of 4, print out yet a different message.
user_num = int(input("Number: "))
if user_num % 2 == 0:
    print("1: Number is even!")

    if user_num % 4 == 0:
        print("1: Number is a multiple of 4!")
else:
    print("1: Number is odd!")


# 2. Use the following list and write a function that prints out all the
#     elements of the list that are less than 5.
arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def less_than_five(li):
    for i in li:
        if i < 5:
            print("2:", i)

less_than_five(arr)


#    b. Instead of printing the elements one by one, make a new list that
#        has all the elements from arr that are less than 5 and print
#        out this new list.
def less_than_five_list(li):
    new_list = []

    for i in li:
        if i < 5:
            new_list.append(i)

    return new_list

print("2b:", less_than_five_list(arr))


# 3. Create a function that asks the user for a number and then prints out a
#     list of all the divisors of that number.
def get_divisors():
    user_num = int(input("Number: "))
    divisors = []
    for i in range(1, user_num + 1):
        if user_num % i == 0:
            divisors.append(i)
    
    print("3:", divisors)

get_divisors()


# 4. Use the following lists and write a function that returns a new list that
#     contains only the elements that are common between the lists (without 
#     duplicates).
arr1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_nums(li1, li2):
    commons = []

    for i1 in li1:
        if i1 in li2 and i1 not in commons:
            commons.append(i1)

    return commons
    # return list(set(li1) & set(li2))  # Same as above.

print("4:", common_nums(arr1, arr2))


# 5. Write a function that asks the user for a string and prints out whether
#     this string is a palindrome or not. (A palindrome is a string that
#     reads the same forwards and backwards.)
def is_palindrome():
    user_str = input("Word: ").lower()
    if user_str == user_str[::-1]:
        print("Yay! Palindrome!")
    else:
        print("Boo. Not.")

is_palindrome()
