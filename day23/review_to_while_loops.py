# 1. Create a movies list containing a single tuple. 
#     The tuple should contain a movie title, the director’s 
#     name, the release year of the movie, and the movie’s budget.
movies = [("Dune: Part Two", "Denis Villeneuve", "2024", 190_000_000)]

#    b. Use an f-string to print the movie name and release year 
#        by accessing your new movie tuple.
# movie_one = movies[0]
# print("1b:", movie_one[0], movie_one[2])
print("1b:", movies[0][0], movies[0][2])  # Same as above, without variable

#    c. Add another new movie tuple to the movies collection using append.
movies.append(("Interstellar", "Christopher Nolan", "2014", 165_000_000))

#    d. Print both movies in the movies collection.
for movie in movies:
    print("1d:", movie[0], movie[2])

#    e. Remove the first movie from movies.
del movies[0]
print("1e:", movies)


# 2. Below is a list of tuples, where each tuple contains details about an
#     employee of a shop: their name, the number of hours worked last week,
#     and their hourly rate. Print how much each employee is due to be paid
#     at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for worker in employees:
    print("2a:", f"{worker[0]}: ${worker[1] * worker[2]}")

#    b. For the employees above, print out those who are earning an hourly
#        wage above average.
all_rates = 0
for worker in employees:
    all_rates += worker[2]
avg_rate = all_rates / len(employees)

results = []
for worker in employees:
    if worker[2] > avg_rate:
        results.append(worker[0])

print(f"2b: Average: ${round(avg_rate, 2)} Earning above average: {', '.join(results)}")


# 3. Consider the following data structure. Remove all the * that do not have a
#     neighboring *. Then print out the number of *'s that remain.
field = [
    "....**....*..***...*",
    "**..*...**...**.*...",
    "*...***...*...****..",
    "...*********......**",
    "****.........*...***",
    "....*.....*....*...."
]
total_stars = 0
for row in field:
    row = row.replace(".*.", "...")  # Solo stars in middle
    if row.find("*.") == 0:  # Find "*." (solo star) at start of row
        row = "." + row[1:]
    if row.find(".*", -2) != -1:  # Find ".*" (solo star) at end of row
        row = row[:-1] + "."

    total_stars += row.count("*")
    print("3: row:", row)

print("3: total_stars:", total_stars)
