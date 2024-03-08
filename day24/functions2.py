# 1. Write a Python function that takes a list of words and returns the
#     longest word and the length of the longest word.
def longest(words):
    longest_len = 0
    longest_word = ""

    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
            longest_word = word

    return longest_word, longest_len

#    b. Call the function with positional arguments
print("1b: (chimpanzee, 10):", longest(["bear", "tiger", "elephant", "chimpanzee", "giraffe"]))

#    c. Call the function with keyword arguments
print("1c: (watermelon, 10):", longest(["apple", "orange", "eggplant", "watermelon", "grapefruit"]))


# 2. Write a Python function to remove the n-th index character from a
#     nonempty string.
def removeNth(str, pos):
    # str_list = list(str)
    # del str_list[pos]
    # return "".join(str_list)
    return str[:pos] + str[pos+1:]  # Same as above. Maybe cleaner to read?

#    b. Call the function with positional arguments
print("2b: paer:", removeNth("paper", 2))

#    c. Call the function with keyword arguments
print("2b: biccle:", removeNth(pos=3, str="bicycle"))


# 3. Create a function called add_title which takes a name and gender as
#     arguments and returns either "Mr. <name>" or "Ms. <name>"
#     (eg. Calling `add_title("Pam", "F")` returns "Ms. Pam")
def add_title(name, gender):
    if gender == "M":
        return f"Mr. {name}"
    else:
        return f"Ms. {name}"

#    b. Call the function with positional arguments
print("3b: Mr. Bond:", add_title("Bond", "M"))

#    c. Call the function with keyword arguments
print("3c: Ms. Pepper:", add_title(gender="F", name="Pepper"))


# 4. Create a function called multiply_elements which takes a list and a
#     number as arguments. It multiplies each element in the list by the
#     number, and returns the list
def multiply_elements(nums, multiplier):
    for i in range(len(nums)):
        nums[i] *= multiplier

    return nums

#    b. Call the function with positional arguments
print("4b: [2, 4, 6, 8, 10]:", multiply_elements([1, 2, 3, 4, 5], 2))

#    c. Call the function with keyword arguments
print("4c: [30, 20, 15, 40, 10]:", multiply_elements(multiplier=5, nums=[6, 4, 3, 8, 2]))
