# https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#32dc8ea2487b45ebb4c8f224146edced
# Console Input
print("Before")
input_string_var = input("Enter your name: ")
print("After")

print("You said:", input_string_var)

# You can use the input to pause the program.
print(f"Hello, {input_string_var} let me display a important message about your car insurance...")
# You can have the program wait for the user. In this case because
# the subsequent output will scroll the above sentence off the
# screen before they can read it.
input("Press any key to continue...")  # Don't need to store the input
print("And continuing")
for i in range(80):
    print("Displays more lines")  # prints 80 times


# https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#8a7276593029442292553e7c0b1edc57
# Casting to change types
num = 3
# print(num + " musketeers")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(num) + " musketeers")


# https://wcode.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#8020e802c12e4af4b79079f16e61c738
# Exercise: Review to Conditions

