# 1. Create a function that always returns True for every item in a
#     given list. However, if an element is the word "flick", switch
#     to always returning the opposite boolean value.
#    EXAMPLES:
#     flick_switch(["edabit", "flick", "eda", "bit"])
#      # => [True, False, False, False]
#     flick_switch(["flick", 11037, 3.14, 53])
#      # => [False, False, False, False]
#     flick_switch([False, False, "flick", "sheep", "flick"])
#      # => [True, True, False, False, True]
def flick_switch(li):
    result_li = []

    flick_state = False
    for word in li:
        if word == "flick":
            flick_state = not flick_state
        result_li.append(not flick_state)

    return result_li

print("1: [True, False, False, False]", flick_switch(["edabit", "flick", "eda", "bit"]))
print("1: [False, False, False, False]", flick_switch(["flick", 11037, 3.14, 53]))
print("1: [True, True, False, False, True]", flick_switch([False, False, "flick", "sheep", "flick"]))


# 2. Create a function that ends the first word of a phrase with "ed",
#     essentially verbifying a noun.
#    EXAMPLES:
#     verbify("cheese burger")  # => "cheesed burger"
#     verbify("salt water")  # => "salted water"
#     verbify("orange juice")  # => "oranged juice"
#     verbify("shredd cheese")  # => "shredded cheese"
def verbify(words):
    tokens = words.split()
    if tokens[0][-1] == "e":  # If last letter of first word is an 'e'
        tokens[0] = tokens[0][:-1]  # Remove the last letter of the first word
    return tokens[0] + "ed " + tokens[1]

print("2: cheesed burger:", verbify("cheese burger"))
print("2: salted water: ", verbify("salt water"))
print("2: oranged juice:", verbify("orange juice"))
print("2: shredded cheese:", verbify("shredd cheese"))
