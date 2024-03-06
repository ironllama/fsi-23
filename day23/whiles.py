# 1. Reverse the following integer number:
# Gonna use swaps!
num = 83275
num = list(str(num))
i = 0  # To count loop runs
# Only swap with first half. Otherwise, you'll swap back to the original number.
while i < (len(num) // 2):
    r_pos = -(i + 1)  # Other side of the swap
    num[i], num[r_pos] = num[r_pos], num[i]
    i += 1
print("1:", int("".join(num)))

# 2. Display the subsequent cubes of the following number up to 1 million:
grow = 3
while True:
    grow = grow**3
    if grow > 1_000_000:
        break
    print("2:", grow)

# 3. Ask the user for numbers until they enter no number. Then throw out the
#     max and min numbers (if max or min appear more than once, throw those
#     out, as well) and print out the mean of all the numbers up to 2
#     decimal places.
all_nums = []
min_num = float('inf')
max_num = 0
while True:
    new_input = input("Enter a number, please: ")
    if new_input == "":
        break

    new_input = int(new_input)
    all_nums.append(new_input)

    # if new_input < min_num:
    #     min_num = new_input
    # if new_input > max_num:
    #     max_num = new_input
    min_num = min(min_num, new_input)  # Same as above
    max_num = max(max_num, new_input)

print("3: all_nums:", all_nums, "min:", min_num, "max:", max_num)

# Deleting min/max. Using a loop in case there is more than 1 of min/max.
while min_num in all_nums:
    del all_nums[all_nums.index(min_num)]
while max_num in all_nums:
    del all_nums[all_nums.index(max_num)]

print("3: all_nums, min/max removed:", all_nums)

num_avg = sum(all_nums) / len(all_nums)
print("3:", round(num_avg, 2))  # Using round to get specific decimal points.
