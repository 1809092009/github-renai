countries = ["Japan", "Italy", "Australia", "Canada", "France"]

# Print the original list
print("Original list:")
print(countries)

# Access an element
print("\nFirst country:")
print(countries[0])

# Modify an element
countries[1] = "Germany"
print("\nAfter modifying an element:")
print(countries)

# Append an element
countries.append("South Korea")
print("\nAfter append():")
print(countries)

# Insert an element
countries.insert(2, "Switzerland")
print("\nAfter insert():")
print(countries)

# Delete an element
del countries[3]
print("\nAfter del:")
print(countries)

# Pop an element
popped_country = countries.pop()
print("\nPopped country:")
print(popped_country)
print(countries)

# Remove an element
countries.remove("France")
print("\nAfter remove():")
print(countries)

# Sort the list alphabetically
countries.sort()
print("\nAlphabetical order:")
print(countries)

# Sort the list in reverse-alphabetical order
countries.sort(reverse=True)
print("\nReverse-alphabetical order:")
print(countries)

# Use sorted() without changing the original list
print("\nUsing sorted():")
print(sorted(countries))

# Reverse the list
countries.reverse()
print("\nAfter reverse():")
print(countries)

# Count the number of elements
print("\nNumber of countries:")
print(len(countries))