# String equality and inequality
name = "Renai"

print(name == "Renai")
print(name != "Andi")

# Using lower()
name = "RENAI"

print(name.lower() == "renai")
print(name.lower() == "andi")

# Numerical tests
number = 15

print(number == 15)
print(number != 10)
print(number > 10)
print(number < 20)
print(number >= 15)
print(number <= 15)

# Using and keyword
age = 17

print(age >= 13 and age <= 19)
print(age < 13 and age > 20)

# Using or keyword
print(age < 13 or age == 17)
print(age > 20 or age == 10)

# Test whether an item is in a list
fruits = ["apple", "banana", "orange"]

print("apple" in fruits)
print("grape" in fruits)

# Test whether an item is not in a list
print("grape" not in fruits)
print("banana" not in fruits)