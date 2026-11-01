pizzas = ["pepperoni", "cheese", "mushroom"]

friend_pizzas = pizzas[:]

# Add a new pizza to the original list
pizzas.append("bbq chicken")

# Add a different pizza to friend_pizzas
friend_pizzas.append("tuna")

# Print my favorite pizzas
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

# Print my friend's favorite pizzas
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)