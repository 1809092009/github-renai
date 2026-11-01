guest_list = ["Isaac Newton", "Albert Einstein", "Thomas Edison",
              "Leonardo da Vinci", "Marie Curie", "Charles Darwin"]

print("Unfortunately, I can invite only two people for dinner.")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print(f"{guest_list[0]}, you are still invited to dinner.")
print(f"{guest_list[1]}, you are still invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)