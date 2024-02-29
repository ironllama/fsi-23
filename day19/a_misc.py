# https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#a26d68d4b8204651baa7c50fdcafe85e
# Conditions: if, elif, else
some_var = 20

if some_var < 10:
    print("some_var is totally less than 10.")
    print("More stuff")
    print("All inside the same block")
    print("Only seen if > 10")
# elif some_var < 10:    # 'elif' is optional, but can be on same line
else:
    if some_var == 10:  # Syntax error, colon must follow 'else'. Can't have anything after colon.
        print("some_var is indeed 10.")
    else:                  # also optional
        if some_var % 5 == 0:
            print("some_var is greater than 10 and a multiple of 5.")
        else:
            if some_var % 3 == 0:
                print("some_var is greater than 10 and a multiple of 3")
            else:
                print("Greater than 10 and not a multiple of 5 or 3")

if some_var < 10:
    print("some_var is totally less than 10.")
    print("More stuff")
    print("All inside the same block")
    print("Only seen if > 10")
elif some_var == 10:    # 'elif' is optional, but can be on same line
    print("some_var is indeed 10.")
elif some_var % 5 == 0:
    print("some_var is greater than 10 and a multiple of 5.")
elif some_var % 3 == 0:
    print("some_var is greater than 10 and a multiple of 3")
else:                  # also optional
    print("Greater than 10 and not a multiple of 5 or 3")
