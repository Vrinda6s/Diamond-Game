import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 60, 90
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load Card Images
card_images = {}
suits = ['hearts', 'spades', 'clubs']
for suit in suits:
    card_images[suit] = {}
    for value in range(2, 15):
        filename = f'{value}_of_{suit}.png'
        card_images[suit][value] = pygame.image.load(os.path.join(suit, filename))

# Create Player Class
class Player:
    def __init__(self, name, assigned_suit):
        self.name = name
        self.assigned_suit = assigned_suit
        self.hand = []
        self.used_cards = []

    def deal_hand(self, deck):
        self.hand = [card for card in deck if card[1] == self.assigned_suit]

    def bid(self, diamond_card):
        available_cards = [card for card in self.hand if card not in self.used_cards]
        return random.choice(available_cards)

# Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diamond Bidding Game")

# Font
font = pygame.font.Font(None, 36)

# Function to display player's hand
def display_hand(player):
    x, y = 50, HEIGHT - CARD_HEIGHT - 20
    for card in player.hand:
        suit = card[1]
        value = card[0]
        card_img = card_images[suit][value]
        screen.blit(card_img, (x, y))
        x += CARD_WIDTH + 10

# Function to display scoreboard
def display_scoreboard(round_num, score_player1, score_player2):
    text_player1 = font.render(f"Player 1: {score_player1} points", True, BLACK)
    text_player2 = font.render(f"Player 2: {score_player2} points", True, BLACK)
    text_round = font.render(f"Round: {round_num}", True, BLACK)
    screen.blit(text_player1, (20, 20))
    screen.blit(text_player2, (20, 60))
    screen.blit(text_round, (WIDTH - 150, 20))

# Function to reveal bids
def reveal_bid(player1, player2, round_num, player1_bid, player2_bid, diamond_card):
    print(f"Round {round_num}: Revealing bids for {diamond_card}...")
    print(f"{player1.name} bids {player1_bid[0]} of {player1_bid[1]}, {player2.name} bids {player2_bid[0]} of {player2_bid[1]}.")

# Function to determine winner
def determine_winner(player1_bid, player2_bid, player1, player2, diamond_card, score_player1, score_player2, round_num):
    if player1_bid[0] > player2_bid[0]:
        score_player1 += diamond_card
        print(f"{player1.name} wins round {round_num} with {diamond_card} points!")
    elif player2_bid[0] > player1_bid[0]:
        score_player2 += diamond_card
        print(f"{player2.name} wins round {round_num} with {diamond_card} points!")
    else:
        score_player1 += diamond_card // 2
        score_player2 += diamond_card // 2
        print("Round ends in a tie.")

    return score_player1, score_player2

# Main Function
def main():
    clock = pygame.time.Clock()
    running = True

    # Game Variables
    round_num = 1
    score_player1 = 0
    score_player2 = 0
    deck = [(value, suit) for value in range(2, 15) for suit in ['hearts', 'spades', 'clubs']]
    random.shuffle(deck)
    player1 = Player("Player 1", "spades")
    player2 = Player("Computer", "hearts")
    player1.deal_hand(deck)
    player2.deal_hand(deck)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Display Player's Hand
        display_hand(player1)

        # Display Bidding Card
        bidding_card = deck[round_num - 1]
        suit = bidding_card[1]
        value = bidding_card[0]
        card_img = card_images[suit][value]
        screen.blit(card_img, (WIDTH // 2 - CARD_WIDTH // 2, HEIGHT // 2 - CARD_HEIGHT // 2))

        # Display Scoreboard
        display_scoreboard(round_num, score_player1, score_player2)

        pygame.display.flip()
        clock.tick(30)  # Ensure smooth frame rate

        # Player 1's Bid
        player1_bid = player1.bid(bidding_card[0])

        # Computer's Bid
        available_cards_player2 = [card for card in player2.hand if card not in player2.used_cards]
        player2_bid = random.choice(available_cards_player2)
        player2.used_cards.append(player2_bid)

        # Reveal Bids
        reveal_bid(player1, player2, round_num, player1_bid, player2_bid, bidding_card[0])

        # Determine Winner
        if player1_bid[0] > player2_bid[0]:
            score_player1 += bidding_card[0]
            print(f"{player1.name} wins round {round_num} with {bidding_card[0]} points!")
        elif player2_bid[0] > player1_bid[0]:
            score_player2 += bidding_card[0]
            print(f"{player2.name} wins round {round_num} with {bidding_card[0]} points!")
        else:
            score_player1 += bidding_card[0] // 2
            score_player2 += bidding_card[0] // 2
            print("Round ends in a tie.")

        # Update Round Number
        round_num += 1

        # Check if all rounds are completed
        if round_num > 13:
            print("Game over! Final scores:")
            print(f"{player1.name}: {score_player1} points")
            print(f"{player2.name}: {score_player2} points")
            if score_player1 > score_player2:
                print(f"{player1.name} wins!")
            elif score_player2 > score_player1:
                print(f"{player2.name} wins!")
            else:
                print("It's a tie!")
            running = False  # End the game loop

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()

