current_users = ["Renai", "Jaden", "Alex", "Sarah", "David"]

new_users = ["RENAI", "Michael", "jaden", "Emma", "Oliver"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is already taken. Please enter a new username.")
    else:
        print(f"{new_user} is available.")