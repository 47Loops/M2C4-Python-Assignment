# > Imports to complete the exercises below:
from decimal import Decimal
import math


# > EXERCISE 1: Create a list, tuple, float, integer, decimal, and dictionary:
towns = ["Barakaldo", "Sestao", "Portugalete", "Santurtzi"] # list
brands = ("Samsung", "Xiaomi", "Apple", "BQ") # tuple
age = 46 # integer
price = 18.20 # float
high = Decimal(1.86) # decimal
persona = {
    "name" : "Manuel",
    "surname" : "Etxebarria",
    "city" : "Zarautz",
    } # dictionary


# > EXERCISE 2: Round your float up:
new_price = math.ceil(price)


# > EXERCISE 3: Get the square root of your float:
square = math.sqrt(price)


# > EXERCISE 4: Select the first element from your dictionary:
first_persona = list(persona.items())[0]


# > EXERCISE 5: Select the second element from your tuple:
new_brands = brands[1]


# > EXERCISE 6: Add an element to the end of your list:
towns.append('Sopuerta')


# > EXERCISE 7: Replace the first element in your list:
towns[0] = "Amoroto"


# > EXERCISE 8: Sort your list alphabetically:
new_list = sorted(towns)


# EXERCISE 9: Use reassignment to add an element to your tuple:
brands += ("Oppo",)