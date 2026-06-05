#Dictionary storing the names and birthdays of Raj's friends
friends_birthdays = {
    "Amit": "October 12",
    "Priya": "March 5",
    "Vikram": "November 20",
    "Sneha": "July 8",
    "Rahul": "January 15"
}

# Raj greets his friends and shares their birthdays with a wish
print("Hello! My name is Raj, and here are the birthdays of my five best friends:")
print("-" * 70)

for name, birthday in friends_birthdays.items():
    print(f"{name}'s birthday is on {birthday}. Best of luck!")
          