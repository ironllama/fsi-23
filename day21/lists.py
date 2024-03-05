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
all_colors += more_colors.strip(",").split(",")
print(all_colors)

# 5. Add a check to make sure the user submitted at least 3 items.
#     If not, print out an appropriate error message to the user and have
#     the Python script run to the end without doing anything more.
if len(more_colors) < 3:
    print("Yo, you need mo' colors!")
    exit()

# 6. Add a check on inserting the user submitted colors into the list.
#     Only add a user submitted color, if it doesn't already exist
#     in the list.

# 7. Again, ask the user for at least 3 colors with one prompt. Do the
#     same input validation (make sure there is at least 3 colors and
#     skip adding any colors that already exist in the all_colors list)
#     but this time add these colors to the front of the list.

# 8. Swap the middle color and the color at the end of the list.
#     If there are an even number of items in the list, bias the
#     middle towards the front of the list. (ie. the middle of four
#     elements would be the second element)

# 9. Move the third to last element to the front.

# 10. Move "red" to the back of the all_colors list.

# 11. Ask the user for a number between 1 and the length of the all_colors
#      list. Actually display the length of the list in the prompt, so
#      the user doesn't have to guess the limit. Create a new list called
#      some_colors with this number of colors from the all_colors list.

# 12. Print out the index of "green" in some_colors list. If it is not in
#      the some_colors list, print out a apologetic message to the user
#      that there is no green in the some_colors list.

# 13. Print out the some_colors list on one line, with "ish" added to
#      each color. (For example: "yellowish greenish orangeish ...")
