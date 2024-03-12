# 1. Find all of the numbers from 1–1000 that are divisible by 8.
print("1:", [num for num in range(8, 1000, 8)])

# 2. Find all of the numbers from 1–1000 that have a 6 in them.
print("2:", [num for num in range(1, 1000) if '6' in str(num)])

# 3. Use the following for the questions below:
string = "Practice Problems to Drill List Comprehension into Your Head."

#    b. Count the number of spaces in a string (use string above).
# print("3b:", string.count(" "))
print("3b:", len([char for char in string if char == " "]))

#    c. Remove all of the vowels in a string (use string above).
# print("3c:", "".join(filter(lambda x: x not in 'aeiou', list(string))))
print("3c:", "".join([char for char in string if char not in 'aeiou']))

#    d. Find all of the words in a string that are less than 5 letters
#        (use string above).
print("3d:", [word for word in string.split() if len(word) < 5])

#    e. Use a dictionary comprehension to count the length of each word in
#        a sentence (use string above).
print("3e:", {word: len(word) for word in string.split()})


# 4. Use the following for the questions below:
nums = [i for i in range(1,1001)]

#    b. Write a list comprehension that produces a list of each number
#        doubled. (use nums list above).
print("4b:", [n + n for n in nums])

#    c. Write a list comprehension that produces a list of the squares of
#        each number (use nums list above).
print("4c:", [n**2 for n in nums])

#    d. Write a list comprehension that produces a list of only the even
#        numbers in that list (use nums list above).
print("4d:", [n for n in nums if n % 2 == 0])

#    e. Write a list comprehension that produces a list of only the odd
#        numbers in that list (use nums list above).
print("4e:", [n for n in nums if n % 2 == 1])

#    f. Write a list comprehension that produces a list of only the positive
#        numbers in that list (use nums list above).
print("4f:", [n for n in nums if n > 0])


# 5. Create a dictionary from the following list with same key:value pairs.
#     eg. {"key": "key"}.
lst = ["NY", "FL", "CA", "VT"]
print("5:", {key: key for key in lst})


# 6. Using dict comprehension, create a dictionary where each number in the
#     range is the key and each item divided by 100 is the value. Use a
#     range from 100 to 160 with steps of 10.
print("6:", {k: k/100 for k in range(100, 160, 10)})


# 7. Using dict comprehension and a conditional argument, create a
#     dictionary from the following dictionary where only the key:value
#     pairs with value above 2000 are taken to the new dictionary.
stonks = { "NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700 }
print("7:", {k:v for k,v in stonks.items() if v > 2000})
