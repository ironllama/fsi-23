from random import randint

# 1. Sort this list of people by age in ascending order without
#     changing the list.
people = [
  {'name': 'Jim', 'salary': 1_000, 'age': 30},
  {'name': 'Bob', 'salary': 2_000, 'age': 260},
  {'name': 'Anne', 'salary': 3_000, 'age': 123},
]
print("1a:", sorted(people, key=lambda p: p['age']))

#    b. Sort by salary in descending order without changing the list.
print("1b:", sorted(people, key=lambda p: p['salary'], reverse=True))

#    c. Sort by their names in ascending order in a way that
#        modifies the list.
people.sort(key=lambda p: p["name"])
print("1c:", people)


# 2. Fill in the missing items in the constructor for the following class.
class Monster:
  def __init__(self, speed, height, health):
    # Fill in here!
    self.speed = speed
    self.height = height
    self.health = health
  
  # Special dunder function used when converting this object into a string
  # For example, when printing. This function will be called.
  # Similar to __str__, too. You can think of the two as:
  # __repr__ for developers (debugging or logging)
  # __str__ for users (UI and reports)
  def __repr__(self):
    # desc = f'Monster: speed->{self.speed}, '
    # desc += f'height->{self.height}, '
    # desc += f'health->{self.health}, '

    # Same as above, but more general -- will handle new properties
    # added, later
    desc = f'Monster: '
    for key, val in vars(self).items():
      desc += f'{key}->{val}, '
    return desc

m1 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m2 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m3 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))
m4 = Monster(randint(1, 100), randint(1, 100), randint(1, 100))

monsters = [m1, m2, m3, m4]

#    b. Sort this list of monsters by speed in ascending order without
#        changing the list.
print("2b by speed:", sorted(monsters, key=lambda m: m.speed))

#    c. Sort this list of monsters by height in descending order
#        without changing the list.
print("2c by height desc:", sorted(monsters, key=lambda m: m.height, reverse=True))

#    d. Sort this list of monsters by health in ascending order
#        without changing the list.
print("2d by health:", sorted(monsters, key=lambda m: m.health))

#    e. Sort this list of monsters by their health x height in
#        ascending order and modify the original list.
# monsters.sort(key=lambda m: m.health * m.height)
# print("2e:", monsters)

for i, m in enumerate(monsters):
  m.name = 'm' + str(i + 1)
  m.vitality = m.health * m.height

monsters.sort(key=lambda m: m.vitality)
# print("2e:", monsters)
print("2e: Sorted by Vitality")
for i, m in enumerate(monsters):
  print(f'[{i + 1}]: {m.name} -- {m.vitality}')
