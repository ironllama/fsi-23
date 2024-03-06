# 1. Use a loop to display elements from the following list that are 
#     present at odd index positions.
num_li = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i, num in enumerate(num_li):
    if i % 2 == 1:
        print("1:", num)

# 2. Filter the following list, so that you only print out the line position
#     and names of people who are 21 or over. Print out all the positions and
#     names comma delimited, with the position in square brackets.
#     (Example output: "[2]: Peter, [3]: Paul, [4]: Mary")
people_in_line = [ 
    ("Boyd", 52),
    ("Mylene", 19),
    ("Retta", 31),
    ("Ethyl", 23),
    ("Irwin", 12),
    ("Murray", 30)
]
output_arr = []
for i, person in enumerate(people_in_line):
    name, age = person
    if age >= 21:
        output_arr.append(f"[{i}]: {name}")
print("2:", ", ".join(output_arr))
