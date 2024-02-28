# Variables x and y refer to Boolean values.
x = True
y = True

# 1. Write an expression that produces True
#    if both variables are True.
print(x and y)

# 2. Write an expression that produces True 
#    if x is False.
# print(x == False)
print(not x)  # Same as above

# 3. Write an expression that produces True 
#    if at least one of the variables is True.
print(x or y)

# 4. Variables full and empty refer to Boolean values. 
#    Write an expression that produces True if at most 
#    one of the variables is True.
# full = True
# empty = False
full = True; empty = False  # Same as above -- semicolons to delimit statements! (Not really Pythonic)
# print("T:", (full == True and empty == False) or (full == False and empty == True))
print("T:", (full and not empty) or (not full and empty))  # Same as above

full = False; empty = True
# print("T:", (full == True and empty == False) or (full == False and empty == True))
print("T:", (full and not empty) or (not full and empty))

full = True; empty = True
# print("F:", (full == True and empty == False) or (full == False and empty == True))
print("F:", (full and not empty) or (not full and empty))

full = False; empty = False
# print("F:", (full == True and empty == False) or (full == False and empty == True))
print("F:", (full and not empty) or (not full and empty))
