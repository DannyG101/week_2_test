def ask_player_action() -> str:
    player_choice = ""
    while not player_choice == "S" and not player_choice == "H":
        player_choice = input("Please choose S or H ").upper()
    return player_choice