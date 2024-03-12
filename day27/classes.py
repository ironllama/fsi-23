import math

# 1. Your task is to create a Circle constructor that creates a circle with a
#     radius provided by an argument. The circles constructed must have two
#     instance methods: getArea() (πr^2) and getCircumference() (2π*r)
#     which give both respective areas and circumference.
#    EXAMPLES:
#     circy = Circle(11)
#     circy.getArea()
#     Should return 380.132711084365

#     circy = Circle(4.44)
#     circy.getCircumference()
#     Should return 27.897342763877365
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def getArea(self):
        return (math.pi * (self.radius**2))

    def getCircumference(self):
        return (2 * math.pi * self.radius)

circy = Circle(11)
print("1: 380.132711084365:", circy.getArea())

circy = Circle(4.44)
print("1: 27.897342763877365:", circy.getCircumference())


# 2. Create methods for the Calculator class that can do the following:
#    - Add two numbers
#    - Subtract two numbers
#    - Multiply two numbers
#    - Divide two numbers
#    EXAMPLES:
#     calculator = Calculator()
#     calculator.add(10, 5)  # => 15
#     calculator.subtract(10, 5)  # => 5
#     calculator.multiply(10, 5)  # => 50
#     calculator.divide(10, 5)  # => 2
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calculator = Calculator()
print("2: 15:", calculator.add(10, 5))
print("2: 5:", calculator.subtract(10, 5))
print("2: 50:", calculator.multiply(10, 5))
print("2: 2:", calculator.divide(10, 5))


# 3. Create a method in the Person class which returns how another person's
#     age compares. Given the objects p1, p2 and p3, which will be
#     initialised with the attributes name and age, return a sentence in
#     the following format:
#     {other_person} is {older than / younger than / the same age as} me.
#    EXAMPLES:
#     p1 = Person("Samuel", 24)
#     p2 = Person("Joel", 36)
#     p3 = Person("Lily", 24)
#     p1.compare_age(p2)  # => "Joel is older than me."
#     p2.compare_age(p1)  # => "Samuel is younger than me."
#     p1.compare_age(p3)  # => "Lily is the same age as me."
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def compare_age(self, other_person):
        compare_str = "older than" if other_person.age > self.age else "younger than" if other_person.age < self.age else "the samge age as"
        return f"{other_person.name} is {compare_str} me."

p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
print("3: older than:", p1.compare_age(p2))
print("3: younger than:", p2.compare_age(p1))
print("3: same age as:", p1.compare_age(p3))


# 4. Create the instance attributes fullname, firstname, lastname and email
#     in an Employee class. Given a person's first and last names:
#    - Form the fullname by simply joining the first and last name together,
#       separated by a space.
#    - Form the email by joining the first and last name together with
#       a . in between, and follow it with @company.com at the end. Make
#       sure the entire email is in lowercase.
#    EXAMPLES:
#     emp_1 = Employee("John", "Smith")
#     emp_2 = Employee("Mary", "Sue")
#     emp_3 = Employee("Antony", "Walker")
#     emp_1.fullname  # => "John Smith"
#     emp_2.email  # => "mary.sue@company.com"
#     emp_3.firstname  # => "Antony"
class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.email = f"{firstname}.{lastname}@company.com".lower()
    
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")
print("4: John Smith:", emp_1.fullname)
print("4: mary.sue@company.com:", emp_2.email)
print("4: Antony:", emp_3.firstname)


# 5. Create a class that takes the following four arguments for a particular
#     football player:
#    - name
#    - age
#    - height
#    - weight
#     Also, create three instance methods for the class that returns the
#     following strings:
#    - get_age() returns "name is age <age>"
#    - get_height() returns "name is <height>cm"
#    - get_weight() returns "name weighs <weight>kg"
#    EXAMPLES:
#     p1 = player("David Jones", 25, 175, 75)
#     p1.get_age()  # => "David Jones is age 25"
#     p1.get_height()  # => "David Jones is 175cm"
#     p1.get_weight()  # => "David Jones weighs 75kg"
class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} is age {self.age}"
    
    def get_height(self):
        return f"{self.name} is {self.height}cm"
    
    def get_weight(self):
        return f"{self.name} weighs {self.weight}kg"

p1 = Player("David Jones", 25, 175, 75)
print("5: David Jones is age 25:", p1.get_age())
print("5: David Jones is 175cm:", p1.get_height())
print("5: David Jones weighs 75kg:", p1.get_weight())
