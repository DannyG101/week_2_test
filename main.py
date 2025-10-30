from core import deck
from core import game_logic

if __name__ == "__main__":
    game_deck = deck.shuffle_by_suit(deck.build_standard_deck())


    player = {"hand" : []}
    dealer = {"hand" : []}

    game_logic.run_full_game(game_deck, player, dealer)
