# 1. Write a function named different that has two parameters, a and b.
#     The function should return True if a and b refer to different values
#     and should return False otherwise.
def different(a, b):
    return a == b

#    b. Call the function with positional arguments
print("1b:", different(5, 6))

#    c. Call the function with keyword arguments
print("1c:", different(b=5, a=6))


# 2. Write a convert_temperatures(t, source, target) function to convert
#     temperature t from source units to target units, where source and
#     target are each one of: "Kelvin", "Celsius", "Fahrenheit", "Rankine",
#     "Delisle", "Newton", "Reaumur", and "Romer" units.
def convert_temperatures(t, source, target):
    # Conversion formula sources:
    # https://www.calculatorsoup.com/calculators/conversions/temperature.php
    # https://live.metric-conversions.org/temperature/

    # Convert all t to Kelvin!
    if source == "Celsius":
        t = t + 273.15
    elif source == "Fahrenheit":
        t = (t + 459.67) * (5/9)
        # t = ((t - 32) / (9/5)) + 273.15
    elif source == "Rankine":
        t = t * (5/9)
    elif source == "Delisle":
        t = ((t + 100) / 1.5) + 273.15
    elif source == "Newton":
        t = (t * (100/33)) + 273.15
    elif source == "Reaumur":
        t = (t * (5/4)) + 273.15
    elif source == "Romer":
        t = ((t - 7.5) * (40/21)) + 273.15
    elif source != "Kelvin":
        print("2: Incompatible source:", source)

    # Convert all Kelvin t to target units!
    if target == "Celsius":
        return t - 273.15
    elif target == "Fahrenheit":
        return (t * (9/5)) - 459.67
        # return ((t - 273.15) * (9/5)) + 32
    elif target == "Rankine":
        return t * (9/5)
    elif target == "Delisle":
        return ((t - 273.15) * 1.5) - 100
    elif target == "Newton":
        return (t - 273.15) / (100/33)
    elif target == "Reaumur":
        return (t - 273.15) * (4/5)
    elif target == "Romer":
        return ((t - 273.15) / (40/21)) + 7.5
    elif target != "Kelvin":
        print("2: Incompatible target:", target)
    
    return t
        
#    b. Call the function with positional arguments
print("2b: 21.63:", round(convert_temperatures(150, "Fahrenheit", "Newton"), 2))

#    c. Call the function with keyword arguments
print("2b: 38.75:", round(convert_temperatures(31, target="Celsius", source="Reaumur"), 2))
print("2b: 101.75:", round(convert_temperatures(31, target="Fahrenheit", source="Reaumur"), 2))
print("2b: 561.42:", round(convert_temperatures(31, target="Rankine", source="Reaumur"), 2))
print("2b: -41.88:", round(convert_temperatures(31, target="Delisle", source="Reaumur"), 2))
print("2b: 12.79:", round(convert_temperatures(31, target="Newton", source="Reaumur"), 2))
print("2b: 31:", round(convert_temperatures(31, target="Reaumur", source="Reaumur"), 2))
print("2b: 311.90:", round(convert_temperatures(31, target="Kelvin", source="Reaumur"), 2))


# 3. Write a function `first_and_last(str, num)` to get a string (str) and
#     num (int). It should return the first 'num' and the last 'num' chars
#     from the given str. If str's length is less than num, return '???'
#     instead of an empty or partial string.
def first_and_last(str, num):
    if len(str) < num:
        return '???'
    
    return [str[:num], str[-num:]]

#    b. Call the function with positional arguments
print("3b:", first_and_last("somethinglong", 4))

#    c. Call the function with keyword arguments
print("3b:", first_and_last(num=2, str="somethinglong"))
print("3b:", first_and_last(num=5, str="dude"))
