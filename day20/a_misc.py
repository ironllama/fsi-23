# # https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#32dc8ea2487b45ebb4c8f224146edced
# # Console Input
# print("Before")
# input_string_var = input("Enter your name: ")
# print("After")

# print("You said:", input_string_var)

# # You can use the input to pause the program.
# print(f"Hello, {input_string_var} let me display a important message about your car insurance...")
# # You can have the program wait for the user. In this case because
# # the subsequent output will scroll the above sentence off the
# # screen before they can read it.
# input("Press any key to continue...")  # Don't need to store the input
# print("And continuing")
# for i in range(80):
#     print("Displays more lines")  # prints 80 times


# # https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#8a7276593029442292553e7c0b1edc57
# # Casting to change types
# num = 3
# # print(num + " musketeers")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(str(num) + " musketeers")


# # https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#8020e802c12e4af4b79079f16e61c738
# # Exercise: Review to Conditions

# https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#467b92fb476d491a9495a643c25e5c48
# Unpacking
# Unpacking copies over properties from different objects
vehicle = { "wheels": 4, "doors": 4 }
car = { "engine": "electric", **vehicle}
print("Car:", car)  # => {'engine': 'electric', 'wheels': 4, 'doors': 4}

print("Vehicle:", vehicle)  # => Still there!
vehicle["wheels"] = 2
vehicle["speed"] = "high"
print("Vehicle:", vehicle)
print("Car:", car)

apple_ratings = { "sweet_lvl": 5, "firm_lvl": 7 }
apple_vis = { "shape": "heart", "color": "red" }
apple = {**apple_ratings, **apple_vis}
print(apple)  # => {'sweet_lvl': 5, 'firm_lvl': 7, 'shape': 'heart', 'color': 'red'}

shoes = { "size": 260, "material": "leather" }
clothes = { "size": "M", "color": "blue", **shoes}  # Size is 260, later value overwrites
print("Clothes:", clothes)

bird = { "name": "Tweedy", "color": "yellow" }
cat = { "name": "Silvester", "legs": 4 }
print("bird_cat:", { **bird, **cat })
print("cat_bird", { **cat, **bird })
