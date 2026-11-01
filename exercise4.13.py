foods = ("fried rice", "fried chicken", "noodles",
         "soup", "salad")

# Print the original menu
print("Original menu:")
for food in foods:
    print(food)

# Try to modify one item
# This will cause a TypeError
# foods[0] = "pizza"

# Create a new tuple with a revised menu
foods = ("pizza", "fried chicken", "pasta",
         "soup", "salad")

print("\nRevised menu:")
for food in foods:
    print(food)