from core.player_io import ask_player_action


def calculate_hand_value(hand: list[dict]) -> int:
    total = 0
    for card in hand:
        if card["rank"] == "J" or card["rank"] == "Q" or card["rank"] == "K":
            total += 10
        elif card["rank"] == "A":
            total += 1
        else:
            total += int(card["rank"])
    return total

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    for i in range(2):
        current_card = deck.pop()
        player["hand"].append(current_card)
    for i in range(2):
        current_card = deck.pop()
        dealer["hand"].append(current_card)
    print(f"Your score is {calculate_hand_value(player["hand"])}")
    print(f"Dealer score is {calculate_hand_value(dealer["hand"])}")

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) <= 17:
        current_card = deck.pop()
        print(current_card)
        dealer["hand"].append(current_card)
    if calculate_hand_value(dealer["hand"]) >= 21:
        print("Dealer has passed 21. You have Won!!")
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:

    deal_two_each(deck, player, dealer)
    player_choice = ask_player_action()
    while not player_choice == "S":
        if player_choice == "H":
            current_card = deck.pop()
            player["hand"].append(current_card)
            if calculate_hand_value(player["hand"]) < 21:
                player_choice = ask_player_action()
            else:
                print(f"You picked a {current_card}")
                print("you have passed 21 and you lose the game!")
                break

    dealer_result = dealer_play(deck, dealer)
    if dealer_result and (calculate_hand_value(player["hand"]) <= 21):
        player_final_result = calculate_hand_value(player["hand"])
        dealer_final_result = calculate_hand_value(dealer["hand"])
        if player_final_result > dealer_final_result:
            print("You have Won!!")
        elif dealer_final_result > player_final_result:
            print("You have lost!")
        else:
            print("Tie break - No one wins")

