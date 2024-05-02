import random

def create_deck():
    suits = ["Spades", "Hearts", "Clubs"]
    values = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    deck = [(suit, value) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def deal_cards(deck, players):
    for player in players:
        player.hand = deck[:13]
        deck = deck[13:]

def calculate_round_winner(bids):
    highest_bid = max(bids, key=lambda x: x[1])
    winners = [player for player, bid in bids if bid == highest_bid[1]]
    return winners

def update_scores(winners, bidding_card):
    for player in winners:
        if player.used_cards[-1][0] == bidding_card[0]:  # If the bid value matches the diamond card value
            player.add_score(bidding_card[1])
        else:  # Penalty for bidding in the wrong suit
            player.add_score(-1)

def start_new_round(deck, players):
    bidding_card = deck.pop(0)
    bids = []
    for player in players:
        player.reset_bids()
        player.bids.append((player, bidding_card))  # Each player automatically bids the first card
        bids.append((player, bidding_card))
    return bids, bidding_card

def check_game_over(players):
    return any(player.score >= 100 for player in players)
