# 1. Create an empty dictionary called monster. Then add the following properties:
#     "damage" property set to 500
#     "defense" property set to 70
#     "weakness" property set to "water"
monster = {}
monster["damage"] = 500
monster["defense"] = 70
monster["weakness"] = "water"

#    b. Do it again, all in one line of Python code
monster = { "damage": 500, "defense": 70, "weakness": "water "}
# monster = {}
# monster.update({ "damage": 500, "defense": 70, "weakness": "water "})  # Also works.

#    c. Set its "name" property to "Gogomish" in a separate line of code
monster["name"] = "Gogomish"
# monster.update({ "name": "Gogomish" })  # Also works.

#    d. Print out the monster
print(monster)
