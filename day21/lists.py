# 1. Create an empty new list called all_colors.
all_colors = []


# 2. Add red, orange, yellow, green, blue, and purple to
#     the all_colors list one item at a time.
all_colors.append("red")
all_colors.append("orange")
all_colors.append("yellow")
all_colors.append("green")
all_colors.append("blue")
all_colors.append("purple")


# 3. Unfortunately, purple was not supposed to be in the list. Can you
#     edit the all_colors list to replace purple with 2 other items,
#     indigo and violet, as the last items in the list?
all_colors.pop()
all_colors += ["indigo", "violet"]


# 4. Ask the user for more input: at least 3 more colors, separated by
#     commas. Parse the input appropriately and insert each of the colors
#     into the all_colors list at the end of the list.
more_colors = input("Enter at least 3 more colors, please: ")
new_colors = more_colors.strip(",").split(", ")
print(new_colors)


# 5. Add a check to make sure the user submitted at least 3 items.
#     If not, print out an appropriate error message to the user and have
#     the Python script run to the end without doing anything more.
if len(new_colors) < 3:
    print("Yo, you need mo' colors!")
    exit()


# 6. Add a check on inserting the user submitted colors into the list.
#     Only add a user submitted color, if it doesn't already exist
#     in the list.
if new_colors[0] not in all_colors:
    all_colors.append(new_colors[0])
if new_colors[1] not in all_colors:
    all_colors.append(new_colors[1])
if new_colors[2] not in new_colors:
    all_colors.append(all_colors[2])
print("6:", all_colors)

# 7. Again, ask the user for at least 3 colors with one prompt. Do the
#     same input validation (make sure there is at least 3 colors and
#     skip adding any colors that already exist in the all_colors list)
#     but this time add these colors to the front of the list.
more_colors = input("Please enter 3 more colors: ")
new_colors = more_colors.strip(",").split(", ")
if len(new_colors) < 3:
    print("Follow directions, man!")
    exit()

# if new_colors[0] not in all_colors:
#     all_colors = [new_colors[0]] + all_colors
#     # all_colors.insert(0, new_colors[0])
# if new_colors[1] not in all_colors:
#     all_colors = [new_colors[1]] + all_colors
#     # all_colors.insert(1, new_colors[0])
# if new_colors[2] not in all_colors:
#     all_colors = [new_colors[2]] + all_colors
#     # all_colors.insert(2, new_colors[0])

if new_colors[0] in all_colors:
    del new_colors[0]
if new_colors[1] in all_colors:
    del new_colors[1]
if new_colors[2] in all_colors:
    del new_colors[2]

all_colors = new_colors + all_colors

print("7:", all_colors)


# 8. Swap the middle color and the color at the end of the list.
#     If there are an even number of items in the list, bias the
#     middle towards the front of the list. (ie. the middle of four
#     elements would be the second element)
middle_pos = (len(all_colors) // 2) - 1
all_colors[middle_pos], all_colors[-1] = all_colors[-1], all_colors[middle_pos]
print("8:", all_colors)


# 9. Move the third to last element to the front.
third_to_last = all_colors.pop(-3)
all_colors.insert(0, third_to_last)
print("9:", all_colors)


# 10. Move "red" to the back of the all_colors list.
red_pos = all_colors.index("red")
red = all_colors.pop(red_pos)
all_colors.append(red)
print("10:", all_colors)


# 11. Ask the user for a number between 1 and the length of the all_colors
#      list. Actually display the length of the list in the prompt, so
#      the user doesn't have to guess the limit. Create a new list called
#      some_colors with this number of colors from the all_colors list.
new_pos = input(f"Gimma number between 1 and {len(all_colors)}: ")
some_colors = all_colors[0:int(new_pos)]


# 12. Print out the index of "green" in some_colors list. If it is not in
#      the some_colors list, print out a apologetic message to the user
#      that there is no green in the some_colors list.
green = False
if "green" in some_colors:
    green_pos = some_colors.index("green")
    if green_pos != -1:
        green = True

if not green:
    print("Sorry, man. A'int there.")


# 13. Print out the some_colors list on one line, with "ish" added to
#      each color. (For example: "yellowish greenish orangeish ...")
print("ish ".join(some_colors) + "ish")
