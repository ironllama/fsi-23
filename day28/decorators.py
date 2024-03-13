# Create a class called Country that has properties for name, population,
# language, and in_europe. Make sure that 'name' is always has a value,
# and 'population' can not be set to a number less than 0. The 'in_europe'
# property must be a boolean and defaults to False. Only the 'language'
# property can be deleted from a Country object.

# Add the appropriate getters and setters for the behavior outlined above,
# and add an additional method called 'grow_pop' that accepts a 'rate'
# argument that will accept a float between -1 and 1 and change the
# Country object's population appropriately.
# EXAMPLE (assume 'spain' is a Country object with population of 1000):
# spain.grow_pop(0.05)  # spain's population is now 1050

# Also include a 'show_lore' function for each object that prints out
# a string in the following format: "<coutry name> is a <terrain>-based
# entity with <population> souls."

# All Country objects share a 'terrain' property set to the string "land".
# Create a method that is shared by all the objects called 'show_kind'
# that prints out "All countries are based on " followed by the current
# value of the 'terrain' property.

# Create at least 5 countries of your choosing, with at least 3 of them
# being in Europe, with the appropriate properties.

# Simulate 1000 years of passing time by adjusting each countries'
# population with a random growth rate annually. Then print out each
# country and their resulting population in the following format:
#  === Population after 1000 years ===
#  <country1 name>: <country1 population>
#  <country2 name>: <country2 population>
#  ... etc.

# Call 'show_lore' for the country with the highest population.

# Then call 'show_lore' for only those countries that are in Europe, that
# still have a population greater than the population they started with
# 1000 years ago.

# Set the terrain property of the Country class to "water" and call 'show_lore'
# with the last country you created. Did it get updated appropriately? Can you
# set just the last country's terrain property to 'fire'? Call the 'show_kind'
# method to show the current value of the terrain for the class to confirm
# that the class is still set to "water".
import random

class Country:

    terrain = "land"

    def __init__(self, name, population, language, in_europe=None):
        self.name = name
        self.population = population
        self.language = language
        self.in_europe = in_europe
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        if val:
            self._name = val
        else:
            print("A valid name value is required!")
    
    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, val):
        if isinstance(val, int) and val >= 0:
            self._population = val
        else:
            print("Population must be an integer greater than 0.")
    
    @property
    def in_europe(self):
        return self._in_europe
    
    @in_europe.setter
    def in_europe(self, val):
        if isinstance(val, bool) and val:
            self._in_europe = val
        else:
            self._in_europe = False

    def grow_pop(self, rate):
        if isinstance(rate, float) and -1 < rate < 1:
            self.population = self.population + round(self.population * rate)
        else:
            print("Growth rate must be a float between -1 and 1.")

    def show_lore(self):
        print(f"{self.name} is a {self.terrain}-based entity with {self.population} souls.")

    @staticmethod
    def show_kind():
        print("All countries are based on " + Country.terrain)
    

belgium = Country("Belgium", 11_697_557, "Flemish", True)
france = Country("France", 68_373_433, "French", True)
spain = Country("Spain", 48_592_909, "Spanish", True)
portugal = Country("Portugal", 10_467_366, "Portuguese", True)
india = Country("India", 1_428_627_663, "Hindi")

all_countries = [belgium, france, spain, portugal, india]
for year in range(1000):
    if year == 999:
        print(f"=== Population after {year + 1} year{'s' if year > 1 else ''} ===")

    for country in all_countries:
        if year == 0:
            country.initial_population = country.population

        country.grow_pop(random.uniform(-0.10, 0.10))

        if year == 999:
            print(f"{country.name}: {country.population}")

print()

high_country = max(all_countries, key=lambda country: country.population)
print("Country with highest population after 1000 years:")
high_country.show_lore()
print()

print("Countries in Europe that grew after 1000 years:")
for country in [c for c in all_countries if c.in_europe]:
    if country.population > country.initial_population:
        country.show_lore()
print()

Country.terrain = "water"
india.show_lore()
india.terrain = "fire"
india.show_lore()
Country.show_kind()
