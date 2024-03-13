from random import randint

# 1. Sort this list of people by age in ascending order without
#     changing the list.
people = [
  {'name': 'Jim', 'salary': 1_000, 'age': 30},
  {'name': 'Bob', 'salary': 2_000, 'age': 260},
  {'name': 'Anne', 'salary': 3_000, 'age': 123},
]

#    b. Sort by salary in descending order without changing the list.

#    c. Sort by their names in ascending order in a way that
#        modifies the list.


# 2. Fill in the missing items in the constructor for the following class.
class Monster:
  def __init__(self, speed, height, health):
    # Fill in here!
  
  def __repr__(self):
    desc = f'Monster: speed->{self.speed}, '
    desc += f'height->{self.height}, '
    desc += f'health->{self.health}, '
    return desc

m1 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m2 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m3 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m4 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))

monsters = [m1, m2, m3, m4]

#    b. Sort this list of monsters by speed in ascending order without
#        changing the list.

#    c. Sort this list of monsters by height in descending order
#        without changing the list.

#    d. Sort this list of monsters by health in ascending order
#        without changing the list.

#    e. Sort this list of monsters by their health x height in
#        ascending order and modify the original list.