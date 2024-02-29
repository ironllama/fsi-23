# https://staritda.notion.site/Python-Beginners-7f1e41c29e9c4a96a7b81e321d3f9c6c#fed9ba28d8f14471bea9e46e0f857726
# Strings

print(1, "good " "food")  # Not very useful?
print(2, "good food")  # Why not just do this?! Why have the break between strings?!

second = "food"
# print(3, "good " second)  # Does not work -- can't use variables with space concat
print (4, "good " + second)

print (5, "good", "food")

first_name = "Barney"
last_name = "Rubble"
middle_name = "Boulder"

full_name = first_name + " " + middle_name + " " + last_name
print("FULL:", full_name)

reversed_name = last_name + " " + middle_name + " " + first_name
print("REVERSED:", reversed_name)

print("BEG:", "[" + full_name[0] + "]")
print("w/END:", "[" + full_name[0:1] + "]")
print("FIRST:", "[" + full_name[0:6] + "]")
print("LAST:", "[" + full_name[15:21] + "]")
print("LAST:", "[" + full_name[15:15 + len(last_name)] + "]")  # You can use math with the index numbers!

message = "Hello world!"
print("The w:", message[6])

excited = "Wow I am ready to program!"
print("Length of excitement:", len(excited))

new_first = full_name[0:6]
new_last = full_name[15:]  # You can omit the last number to go until the end of the string.
print("FIRST LAST:", new_first, new_last)


# F-strings
name = "Sofia"
age = 31
job = "programmer"

sentence = f"My friend {name} is a {age} year old {job} living in New York."
print(sentence)

print("Ba" + ("na" * 3))

greeting = 'Hi! '
greetings = greeting * 10
print(greetings)

shout = 'hello there'.upper()
print(shout)

whisper = 'SHHHHH'.lower()
print(whisper)

book = 'harry potter'.title()
print(book)

no_js = 'jump jay jump!'.replace('j', '')
print(no_js)

name = 'Joseph'
name += ' Sungpil'
name += ' Choi'
print('full name:', name)
