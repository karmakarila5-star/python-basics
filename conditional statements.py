# Step 1: Ask the user to input the current temperature
temperature = float(input("Enter the current temperature in Celsius: "))

# Step 2: Check the temperature using conditional statements
if temperature >= 25:
    print("It is warm enough! You can wear light and soft clothes safely.")
elif temperature >= 15:
    print("The weather is mild. A light long-sleeve shirt or light layers would be best.")
else:
    print("It is too cold! Keep wearing your jacket or pullover to stay warm.")