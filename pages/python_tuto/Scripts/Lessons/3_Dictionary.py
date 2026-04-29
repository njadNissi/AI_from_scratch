""" 
    Tuple: list of items that cannot be modified (immutable)
    List: list of items that can be modified (mutable)
    Dict: collection of key-value pairs (mutable)
"""

tuple_x = ()
list_y = []
dict_z = {}

vowels = ("a", "e", "i", "o", "u")
digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# item => key: value
dict_z = {
    "vowels": ("a", "e", "i", "o", "u"),
    "digits": (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    10: "ten",
    "twenty": 20
}

# print(dict_z)
# print(dict_z["vowels"])

# digits = dict_z["digits"]
# print(f"Digits: {digits}")

# digit_7 = dict_z["digits"][-3]
# print(f"Digit_7: {digit_7}")


list1 = [1, 2, 3, [4, 5, [6, 7]]]
element_6 = list1[-1][-1][0]

# example: a dictionary of cars with properties.
# A dictionary of 10 cars with diverse properties
cars_dictionary = {
    "car_1": {
        "color": "Midnight Black",
        "type": "Sedan",
        "mark": "Toyota",
        "model": "Camry",
        "series": "XSE",
        "year": 2024,
        "fuel_type": "Hybrid",
        "horsepower": 208,
        "transmission": "8-speed automatic"
    },
    "car_2": {
        "color": "Ocean Blue Metallic",
        "type": "SUV",
        "mark": "Ford",
        "model": "Explorer",
        "series": "Platinum",
        "year": 2023,
        "fuel_type": "Gasoline",
        "horsepower": 300,
        "transmission": "10-speed automatic"
    },
    "car_3": {
        "color": "Rosso Corsa (Red)",
        "type": "Sports Car",
        "mark": "Ferrari",
        "model": "F8 Tributo",
        "series": "Base",
        "year": 2022,
        "fuel_type": "Gasoline",
        "horsepower": 710,
        "transmission": "7-speed dual-clutch"
    },
    "car_4": {
        "color": "Glacier White",
        "type": "Hatchback",
        "mark": "Volkswagen",
        "model": "Golf",
        "series": "GTI",
        "year": 2024,
        "fuel_type": "Gasoline",
        "horsepower": 241,
        "transmission": "7-speed DSG automatic"
    },
    "car_5": {
        "color": "Pearl White Multi-Coat",
        "type": "Electric Sedan",
        "mark": "Tesla",
        "model": "Model 3",
        "series": "Performance",
        "year": 2023,
        "fuel_type": "Electric",
        "horsepower": 450,
        "transmission": "Single-speed fixed gear"
    },
    "car_6": {
        "color": "Cyber Orange Metallic Tri-Coat",
        "type": "Pickup Truck",
        "mark": "Ford",
        "model": "F-150",
        "series": "Raptor",
        "year": 2024,
        "fuel_type": "Gasoline",
        "horsepower": 450,
        "transmission": "10-speed automatic"
    },
    "car_7": {
        "color": "Saphire Blue Metallic",
        "type": "Luxury SUV",
        "mark": "BMW",
        "model": "X5",
        "series": "xDrive40i",
        "year": 2023,
        "fuel_type": "Gasoline",
        "horsepower": 335,
        "transmission": "8-speed automatic"
    },
    "car_8": {
        "color": "Mojave Sand",
        "type": "Compact SUV",
        "mark": "Honda",
        "model": "CR-V",
        "series": "EX-L",
        "year": 2024,
        "fuel_type": "Hybrid",
        "horsepower": 204,
        "transmission": "e-CVT"
    },
    "car_9": {
        "color": "Obsidian Black",
        "type": "Luxury Sedan",
        "mark": "Mercedes-Benz",
        "model": "S-Class",
        "series": "S 580",
        "year": 2023,
        "fuel_type": "Gasoline",
        "horsepower": 496,
        "transmission": "9-speed automatic"
    },
    "car_10": {
        "color": "Deep Forest Green",
        "type": "Electric SUV",
        "mark": "Jaguar",
        "model": "I-PACE",
        "series": "EV400 SE",
        "year": 2024,
        "fuel_type": "Electric",
        "horsepower": 394,
        "transmission": "Single-speed automatic"
    }
}
# print(cars_dictionary)
"""
    print(f"car 1 - color : {cars_dictionary['car_1']['color']}")
    print(f"car 1 - horsepower : {cars_dictionary['car_1']['horsepower']}")
    print(f"car 1 - year : {cars_dictionary['car_1']['year']}")
    print(f"car 1 - fuel_type : {cars_dictionary['car_1']['fuel_type']}")
    print(f"car 1 - transmission : {cars_dictionary['car_1']['transmission']}")
    print(f"car 2 - color : {cars_dictionary['car_2']['color']}")

    HOWEWORK: print this style using index-wise and item-wise for loop.
    car_1
        color: "Obsidian Black",
        type: "Luxury Sedan",
        mark: "Mercedes-Benz",
        model: "S-Class",
        series: "S 580",
        year: 2023,
        fuel_type: "Gasoline",
        horsepower: 496,
        transmission: "9-speed automatic"

    car_2
        color: "Deep Forest Green",
        type: "Electric SUV",
        mark: "Jaguar",
        ...
"""

# cars_keys = cars_dictionary.keys()
# print(f"Cars keys: {cars_keys}")
# for key in cars_keys:
#     value = cars_dictionary[key]
#     print(key)




# cars_values = cars_dictionary.values()
# print(f"Cars values: {cars_values}")

# cars_items = cars_dictionary.items()
# print(f"Cars items: {cars_items}")



# ------
# 1. Range: generator, can be stored in a variable.
# *: unpacking operator to convert range to list.
range_2_9 = [*range(2, 10, 2)]
print(f"Range 2-9: {range_2_9}")

# zip: combine two or more iterables into a single iterable of tuples.
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
for item in zip(l1, l2):
    print(item) # item = (el_l1, el_l2)
    
for el_l1, el_l2 in zip(l1, l2):
    print(f"{el_l1*2}: {el_l2*3}")
    
print("\n---\n")
######> D.items() = zip(D.keys(), D.values())
car = {
    "color": "Midnight Black",
    "type": "Sedan",
    "mark": "Toyota",
    "model": "Camry",
    "series": "XSE",
    "year": 2024,
    "fuel_type": "Hybrid",
    "horsepower": 208,
    "transmission": "8-speed automatic"
}
# Method1: using index-wise loop
for key in car.keys():
    value = car[key]
    print(f"{key}: {value}")
    
print("\n---\n")

# Method2: using item-wise loop
for key, value in car.items():
    print(f"{key}: {value}")