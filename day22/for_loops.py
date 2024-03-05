# 1. Print the first 10 natural numbers.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    print("1:", n)


# 2. Print the following pattern:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
nums = [1, 2, 3, 4, 5]

# new_nums = []  # To store the growing list, as we add to it.
# for n in nums:
#     new_nums.append(str(n))  # Add to it, but add as str for join
#     print("2:", " ".join(new_nums))

# Create a new list of strs, instead of nums
num_strs = []
for n in nums:
    num_strs.append(str(n))

for n in num_strs:  # Use the list of strs
    new_slice = num_strs[0:int(n)]  # Use the n to help slice
    print("2:", " ".join(new_slice))


# 3. Print the first 10 multiples of a given number on a single line.
#     For example: 2 4 6 8 10 12 14 16 18 20
list_of_strs = []
indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in indexes:
    list_of_strs.append(str(i * 2))
print("3:", " ".join(list_of_strs))

# 4. Given the following list, display numbers divisible by five, 
#     and if you find a number greater than 150, stop the loop.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for num in list1:
    if num > 150:
        break
    if num % 5 == 0:
        print(num)

# 5. Display numbers from -10 to -1.
indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in indexes:
    print("5:", i - 10)
    