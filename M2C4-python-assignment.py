# > Imports to complete the exercises.
import math


# > EXERCISE 1: Create a list, tuple, float, integer, decimal, and dictionary.
towns = ["Barakaldo", "Sestao", "Portugalete", "Santurtzi"]
brands = ("Samsung", "Xiaomi", "Apple", "BQ")
age = 46
price = 18.20
persona = {
    "name" : "Manuel",
    "surname" : "Etxebarria",
    "city" : "Zarautz",
    }


# > EXERCISE 2: Round your float up.
new_price = math.ceil(price)
print(new_price)


# > EXERCISE 3: Get the square root of your float.
square = math.sqrt(price)
print(square)


# > EXERCISE 4: Select the first element from your dictionary.
first_persona = list(persona.keys())[0]
print(first_persona)


# > EXERCISE 5: Select the second element from your tuple.
new_brands = brands[1]
print(new_brands)


# > EXERCISE 6: Add an element to the end of your list.
towns.append('Sopuerta')
print(towns)


# > EXERCISE 7: Replace the first element in your list.
towns[0] = "Amoroto"
print(towns)


# > EXERCISE 8: Sort your list alphabetically.
new_list = sorted(towns)
print(new_list)


# EXERCISE 9: Use reassignment to add an element to your tuple.
brands += ("Realme", "Oppo")
print(brands)