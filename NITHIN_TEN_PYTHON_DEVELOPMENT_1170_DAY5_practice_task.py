# =========================================
# TASK 1: Create a list of 5 fruits
# =========================================
print("\nTASK 1: LIST OF 5 FRUITS")
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

for fruit in fruits:
    print(fruit)


# =========================================
# TASK 2: Create a tuple of 3 colors
# =========================================
print("\nTASK 2: TUPLE OF COLORS")
colors = ("Red", "Green", "Blue")

print("All colors:", colors)
print("First color:", colors[0])


# =========================================
# TASK 3: Dictionary with student names and marks
# =========================================
print("\nTASK 3: STUDENT MARKS DICTIONARY")
students = {
    "Nithin": 85,
    "Sanjay": 90,
    "Sara": 88
}

for name, marks in students.items():
    print(name, ":", marks)


# =========================================
# TASK 4: Set of 5 numbers (unique values)
# =========================================
print("\nTASK 4: UNIQUE NUMBERS USING SET")
numbers = {1, 2, 2, 3, 4, 4, 5}

print("Unique numbers:", numbers)


# =========================================
# TASK 5: Dictionary of products and quantities
# =========================================
print("\nTASK 5: PRODUCT STOCK DETAILS")
products = {
    "Laptop": 10,
    "Mouse": 50,
    "Keyboard": 30,
    "Monitor": 15
}

for product, qty in products.items():
    print(product, ":", qty)