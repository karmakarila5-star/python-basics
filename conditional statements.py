while True:
    user_input = input("Enter a character (or type 'quit' to stop): ")

    if user_input == "quit":
        print("Goodbye!")
        break

    if len(user_input) == 0:
        print("Error: You did not type anything.")
    elif len(user_input) > 1:
        print("Error: You typed more than one character.")
    else:
        if user_input.isalpha():
            print(f"'{user_input}' is an alphabet.")
        else:
            print(f"'{user_input}' is not an alphabet.")
