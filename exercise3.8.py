places = ["Japan", "Switzerland", "South Korea", "Italy", "Australia"]

# Print the list in its original order
print(places)

# Print the list in alphabetical order
print(sorted(places))

# Show that the list is still in its original order
print(places)

# Print the list in reverse-alphabetical order
print(sorted(places, reverse=True))

# Show that the list is still in its original order
print(places)

# Change the order of the list
places.reverse()
print(places)

# Change the order of the list back to its original order
places.reverse()
print(places)

# Change the list to alphabetical order
places.sort()
print(places)

# Change the list to reverse-alphabetical order
places.sort(reverse=True)
print(places)