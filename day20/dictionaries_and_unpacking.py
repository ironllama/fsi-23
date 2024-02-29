# 1. Create a dictionary called ruby with "beautiful" set to True
ruby = { "beautiful": True }

# 2. Create a dictionary called shield with "sturdy" set to False
shield = { "sturdy": False }

# 3. Create a dictionary called ruby_shield by unpacking ruby and shield into it
ruby_shield = {**ruby, **shield}

# 4. Print out ruby_shield
print("ruby_shield:", ruby_shield)
