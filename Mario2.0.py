def mario_game():

    mario_char = """
        ______
       /      \
      /        \
     /|  O  O  |\
      |   /|\  |
     /|   \|/  |\
    / |        | \
     /| ------ |\
    / | _****_ | \
      |        |
     _|________|_
    """
 
    # Print the initial Mario character
    print(mario_char)
 
    # Start the game loop
    while True:
        # Prompt the user for input
        user_input = input("Enter a command (u, l, d, r, q): ")
 
        # Check the user's input and perform the corresponding action
        if user_input.lower() == 'u':
            print("Moving Mario up!")
        elif user_input.lower() == 'l':
            print("Moving Mario left!")
        elif user_input.lower() == 'd':
            print("Moving Mario down!")
        elif user_input.lower() == 'r':
            print("Moving Mario right!")
        elif user_input.lower() == 'q':
            print("Quit: Good Game")
            break
        else:
            print("Invalid command! Please try again.")
 
# Call the create_mario_game function to start the game
mario_game()
