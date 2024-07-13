import text_utils

# prints menu and sends to function based on user input
while True: 
    string = input("Please type the string you would like to use: ")
    menu_selection = input("\n----------------------------\n\tString Manipulation Menu\n1. Reverse String\n2. Convert String to Uppercase\n3. Convert String to Lowercase\n4. Checks if String is Alphabet Characters\n---------------------------")
    while True:
        if menu_selection == '1': 
            print(text_utils.reverse_string(string))
            break
        if menu_selection == '2': 
            print(text_utils.upper_string(string))
            break
        if menu_selection == '3': 
            print(text_utils.lower_string(string))
            break
        if menu_selection == '4': 
            print(text_utils.check_alpha(string))
            break
        else:
            menu_selection = input("\nPlease type one of the menu values (1-4): ")

    # ask the user if they would like to try again 
    try_again = input ("\nWould you like to try anther string? (Y,N): ")
    while try_again not in ["Y", "N"]: 
        try_again = input ("\nWould you like to try anther string? (Y,N): ")
    if try_again == "N":
        break
