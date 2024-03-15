# 1. Ask the user for the name of a cocktail. Then use the Cocktails DB
# (https://www.thecocktaildb.com/) to get data about the drink. List
# all the ingredients on separate lines sorted alphabetically. Then,
# below the ingredients, show the directions on how to make the
# cocktail. (English) If the cocktail name does not exist then let the
# user know. Regardless, ask again for another cocktail name. If the
# user types 'q', then stop asking and end the program.
import requests

while True:
    user_input = input("What cocktail would you like to make? ('q' to quit): ")
    if user_input == 'q':
        break

    response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=" + user_input).json()
    if ("drinks" in response  # If response has a property called "drinks"
            and response["drinks"]  # If it is not null/None and is not empty
        ):
        drink = response["drinks"][0]
        print(f"===== {drink['strDrink']} =====")

        print(f"Ingredients:")
        for i in range(15):
            new_ingredient = "strIngredient" + str(i + 1)
            if new_ingredient in drink and drink[new_ingredient]:
                print(f"{drink[new_ingredient]} -- {drink['strMeasure' + str(i + 1)]}")
            else:
                break
        print()

        print(f"Directions:")
        print(drink["strInstructions"])
        print()
    else:
        print(f"\tCan't seem to find a cocktail called {user_input}!")
