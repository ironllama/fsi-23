# 1. Get a 3-digit number from the user. Ask that all three digits are
#     different numbers. Store this number in a variable called 'first_num'.
first_num = input("Gimme a 3-digit number, with different digits: ")

# 2. Validate that all 3 digits are different numbers. If not, instruct
#    the user to run the exercise again with a valid number and stop
#    running the rest of the code by calling 'exit()'.
if first_num[0] == first_num[1] or first_num[1] == first_num[2] or first_num[0] == first_num[2]:
    print("Please ensure all digits are different!")
    exit()

# 3. Reverse the 3 digits in first_num, without using the list 'reverse'
#    or 'reversed' functions. Use only what you've learned so far.
#    Save this reversed number in another variable called 'second_num'.
# second_num = first_num[::-1]
second_num = first_num[2] + first_num[1] + first_num[0]

# 4. Subtract second_num from first_num and store the result in another
#    variable called 'third_num'. If third_num is a negative number
#    turn it into a positive number.
first_num = int(first_num)
second_num = int(second_num)
third_num = first_num - second_num
# if third_num < 0:
#   third_num = -third_num
# if third_num < 0:
#   third_num *= -1
third_num = abs(third_num)

# 5. Reverse third_num and save it to a variable called 'fourth_num'.
fourth_num = str(third_num)[::-1]

# 6. Add third_num and fourth_num and print out the result. (1089)
print("6. (1089):", third_num + int(fourth_num))

# 7. Subtract the lesser number of first_num and second_num from the
#    greater number of first_num and second_num so that you end up
#    with a positive number for the difference. Save this difference
#    in a variable called 'fs_diff'.
if first_num > second_num:
    fs_diff = first_num - second_num
else:
    fs_diff = second_num - first_num


# 8. Add up the individual digits that make up fs_diff and print out
#    the resulting sum. (18)
fs_diff_str = str(fs_diff)
print("8. (18):", int(fs_diff_str[0]) + int(fs_diff_str[1]) + int(fs_diff_str[2]))
