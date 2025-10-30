import random

def build_standard_deck() -> list[dict]:
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["D", "H", "S", "C"]
    full_deck = []
    for suit in suits:
        for card in cards:
            current_card = {"rank" : card, "suit" : suit}
            full_deck.append(current_card)
    return full_deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    mix_count = 0
    while mix_count <swaps:
        index1 = random.randint(0, 51)
        index2 = random.randint(0, 51)
        if index1 != index2:
            deck[index1], deck[index2] = deck[index2], deck[index1]
            mix_count += 1
    return deck

#I tried the below
    # mix_count = 0
    # while mix_count < swaps:
    #     i = random.randint(0, 51)
    #     j = random.randint(0, 51)
    #     if i != j:
    #         if deck[i]["suit"] == "A" or deck[i]["rank"] == "J" or deck[i]["suit"] == "Q" or deck[i]["suit"] == "K":
    #             pass
    #         if deck[i]["suit"] == "H" and int(deck[j]["rank"]) % 5 == 0:
    #             deck[i], deck[j] = deck[j], deck[i]
    #             mix_count += 1
    #         if deck[i]["suit"] == "C" and int(deck[j]["rank"]) % 3 == 0:
    #             deck[i], deck[j] = deck[j], deck[i]
    #             mix_count += 1
    #         if deck[i]["suit"] == "D" and int(deck[j]["rank"]) % 2 == 0:
    #             deck[i], deck[j] = deck[j], deck[i]
    #             mix_count += 1
    #         if deck[i]["suit"] == "S" and int(deck[j]["rank"]) % 7 == 0:
    #             deck[i], deck[j] = deck[j], deck[i]
    #             mix_count += 1
    # return deck