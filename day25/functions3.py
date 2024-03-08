# 1. Write a function to find the largest of three numbers, without using
#     the built-in `max` function.
def largest_num(one, two, three):
    largest = one

    if two > largest:
        largest = two
    if three > largest:
        largest = three

    return largest

print("1: 45:", largest_num(45, 23, 12))
print("1: 38321:", largest_num(18378, 38321, 234))
print("1: -283:", largest_num(-324, -48583, -283))


# 2. Write a function to sum all the numbers in a list, without using the
#     built-in `sum` function.
def sum_nums(nums):
    if nums:
        sum = nums[0]
    else:
        sum = 0

    for n in nums[1:]:
        sum += n

    return sum

print("2: 15:", sum_nums([0, 1, 2, 3, 4, 5]))
print("2: -3:", sum_nums([-5, -4, 3, 2, 1]))
print("2: 0:", sum_nums([]))


# 3. Write a function to multiply all the numbers in a list, without using
#     any library functions.
def product_nums(nums):
    if len(nums) > 0:
        prod = nums[0]
    else:
        prod = 0

    for n in nums[1:]:
        prod *= n

    return prod

print("3: 0:", product_nums([0, 1, 2, 3, 4, 5]))
print("3: 120:", product_nums([1, 2, 3, 4, 5]))
print("3: -120:", product_nums([-5, -4, -3, 2, 1]))
print("3: 0:", product_nums([]))


# 4. Write a function to reverse a string, without using the built-in
#     `reverse` function.
def reverse_str(in_str):
    return in_str[::-1]

print("4: elppa:", reverse_str("apple"))
print("4: 4851:", reverse_str("1584"))
print("4: a:", reverse_str("a"))


# 5. Write a function to check whether a number falls in a given range.
def in_range(num, start, end):
    return num in range(start, end + 1)

print("5: True:", in_range(5, 1, 7))
print("5: False:", in_range(-5, 1, 7))
print("5: True:", in_range(23, 15, 23))
print("5: True:", in_range(2, 2, 2))


# 6. Write a function that takes a list and returns a new list with
#     unique elements of the first list.
def get_unique(nums):
    return list(set(nums))

print("6: [1, 2, 3, 4, 5, 6]:", get_unique([5, 3, 6, 2, 4, 3, 2, 5, 1]))
print("6: [3, 5]:", get_unique([5, 3, 3, 5]))


# 7. Write a function that takes a number as a parameter and checks if the
#     number is prime or not.
def is_prime(num):
    if num in [0, 1, 2]:
        return True

    if num % 2 == 0:
        return False

    half = num // 2
    for i in range(3, half, 2):
        if num % i == 0:
            return False
    
    return True

print("7: True:", is_prime(13))
print("7: True:", is_prime(2))
print("7: False:", is_prime(88))
print("7: True:", is_prime(25964951))


# 8. Write a function to print only the even numbers from a given list.
def get_evens(nums):
    new_list = []

    for n in nums:
        if n % 2 == 0:
            new_list.append(n)

    return new_list

print("8: [8, 4, 8, 2, 342]:", get_evens([8, 4, 7, 3, 8, 2, 349, 3827, 342]))
print("8: []:", get_evens([3, 5, 7]))


# 9. Write a function to create and print the list of squares for the
#      numbers between 1 and 30 (both included).
def get_squares_to_30():
    total = []

    for i in range(1, 31):
        total.append(i * i)

    return total

print("9:", get_squares_to_30())
