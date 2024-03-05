# Repeat the previous exercise using for loops and 'range'.

# 1. Print the first 10 natural numbers.
for num in range(1, 11):
    print("1:", num)

# 2. Print the following pattern:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
new_nums = []
for n in range(1, 6):
    new_nums.append(str(n))  # Add to it, but add as str for join
    print("2:", " ".join(new_nums))

# 3. Print the first 10 multiples of a given number on a single line.
#     For example: 2 4 6 8 10 12 14 16 18 20
num = 2
# new_nums = []
# for i in range(num, (num * 10) + 1, num):
#     new_nums.append((str(i)))
# print("3:", " ".join(new_nums))

for i in range(num, (num * 10) + 1, num):
    print(i, end=" ")
print()  # Reset with newline for next exercise.

# 4. Given the following list, display numbers divisible by five, 
#     and if you find a number greater than 150, stop the loop.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 173, 180, 200]
for num in range(len(list1)):
    if list1[num] > 150:
        break
    if list1[num] % 5 == 0:
        print("4:", list1[num])

# 5. Display numbers from -10 to -1.
# print("5:", list(range(-1, -11, -1))[::-1])
print("5:", list(range(-10, 0)))
