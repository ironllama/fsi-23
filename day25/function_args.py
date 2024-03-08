# 1. Create a function multi_print which takes advantage of *args, accepts
#     any number of positional arguments, and prints them all using a for
#     loop, also print the total number of arguments passed into multi_print.
def multi_print(*args):
    for arg in args:
        print("1:", arg)

    print("1:", len(args))

multi_print("apple", "orange", "lime", "strawberry", "watermelon", "pineapple")


# 2. Create a function that accepts any number of numbers as positional
#     arguments and prints the sum of those numbers.
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    
    return total
    # return sum(args)  # Same as above.

print("2: 21:", sum_all(3, 7, 2, 8, 1))
print("2: 46698:", sum_all(5483, 29823, 238, 21, 2348, 253, 985, 7547))


# 3. Create a function that accepts any number of positional and keyword
#     arguments, and that prints them back to the user. Your output should
#     print the positional arguments on one line, each item separated with
#     the string 'and'. All the keyword arguments should be printed in the
#     format 'key - value', each on a separate line.
#
#    Examples:
#     echo("apple", "pear", "lime", a="8", b="4", c="3")
#    Outputs:
#     apple and pear and lime
#     a - 8
#     b - 4
#     c - 3
#
#     echo("apple", 4, True, a="pear", b=12, c=False)
#    Outputs:
#     apple and 4 and True
#     a - pear
#     b - 12
#     c - False
#
#     echo("apple")
#    Outputs:
#     apple
#
#     echo(a=8, what="sup")
#    Outputs:
#     a - 8
#     what - sup
def echo(*args, **kwargs):
    args = list(args)  # Tuple to list, so we can change/cast items to str
    for i, arg in enumerate(args):
        args[i] = str(arg)
    if args:  # Prevent printing if args is empty
        print("3:", " and ".join(args))

    for k,v in kwargs.items():
        print("3:", k + " - " + str(v))

echo("apple", "pear", "lime", a="8", b="4", c="3")
echo("apple", 4, True, a="pear", b=12, c=False)
echo("apple")
echo(a=8, what="sup")


# 4. Create a function called 'breakup' that accepts any number of strings or
#     lists of strings, and a 'sep' argument. Return all the strings and list
#     of strings combined, separated by the string given in 'sep'.
#    Examples:
#     breakup("red", "green", sep=" and ") => "red and green"
#     breakup("red", "green", "pink", sep=" and ") => "red and green and pink"
#     breakup(["red", "green"], sep=" and ") => "red and green"
#     breakup("pink", ["red"], "green", sep=" and ") => "pink and red and green"
def breakup(*args, sep):
    final_list = []
    for arg in args:
        if isinstance(arg, list):
            final_list += arg
        else:
            final_list.append(arg)
    
    return sep.join(final_list)

print("4: red and green:", breakup("red", "green", sep=" and "))
print("4: red and green and pink:", breakup("red", "green", "pink", sep=" and "))
print("4: red and green:", breakup(["red", "green"], sep=" and "))
print("4: pink and red and green:", breakup("pink", ["red"], "green", sep=" and "))
