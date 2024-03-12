class Person:
  def __init__(yo, name, age):
    yo.name = name
    yo.age = age

p1 = Person("John", 36)

print(p1.name)  # => John
print(p1.age)   # => 36