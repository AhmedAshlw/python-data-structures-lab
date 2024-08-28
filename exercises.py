# Exercise 0: Example
def example_list_function():
    example_list = ["element1", "element2", "element3"]
    for element in example_list:
        print(element)


# Call the function and print each element
example_list_function()
print("==============================")


# Exercise 1: List and Indexing
def manage_students():
    students = ["Mohammed", "Ali", "Hasan"]
    first_student = students[1]
    last_student = students[2]

    return f"{first_student} {last_student}"


# Call the function and print the result
print("Exercise 1:", manage_students())
print("==============================")


# Exercise 2: Loop and String Concatenation
def combine_foods():
    foods = ["Chicken Masala", "Spagiti Poloneez", "Sezleeng"]
    meal = ""
    for meal in foods:
        print(meal)
    return True


# Call the function and print the result
print("Exercise 2:", combine_foods())
print("==============================")


# Exercise 3: Slicing Tuples
def slice_foods():
    foods = ["Chicken Masala", "Spagiti Poloneez", "Sezleeng"]
    last_two_foods = foods[-2], foods[-1]
    return last_two_foods


# Call the function and print the result
print("Exercise 3:", slice_foods())
print("==============================")


# Exercise 4: Dictionaries and String Formatting
def hometown_info():
    home_town = {"city": "Bahrain", "state": "Sanabis", "population": "4000"}
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    return home_town_message


# Call the function and print the result
print("Exercise 4:", hometown_info())
print("==============================")

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"


def list_home_town_items():
    home_town = {"city": "Bahrain", "state": "Sanabis", "population": "4000"}
    for key, val in home_town.items():
        print(f"{key} is {val}")
    return True


# Call the function and print the result
print("Exercise 5:", list_home_town_items())
print("==============================")
