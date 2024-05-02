import pygame
import sys
from player import Player
from game import deal_cards
# Initialize pygame
pygame.init()

# Constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class UI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Diamond Bidding Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def draw_game_board(self):
        self.screen.fill(WHITE)
        self.draw_text("Diamond Bidding Game", BLACK, 20, 20)
        # Draw other UI elements as needed

    def draw_player_hand(self, player, x, y):
        for i, card in enumerate(player.hand):
            card_rect = pygame.Rect(x + i * 80, y, 70, 100)
            pygame.draw.rect(self.screen, BLUE, card_rect)  # Placeholder for card display
            card_text = f"{card[0]} of {card[1]}"
            self.draw_text(card_text, BLACK, x + i * 80 + 5, y + 5)

    def draw_bid_input(self, x, y):
        bid_rect = pygame.Rect(x, y, 200, 50)
        pygame.draw.rect(self.screen, GREEN, bid_rect)  # Placeholder for bid input
        self.draw_text("Enter Bid", BLACK, x + 50, y + 10)

    def draw_scores(self, player1_score, player2_score):
        self.draw_text(f"Player 1 Score: {player1_score}", BLACK, 20, SCREEN_HEIGHT - 80)
        self.draw_text(f"Player 2 Score: {player2_score}", BLACK, 20, SCREEN_HEIGHT - 40)

    def update_screen(self):
        pygame.display.flip()

    def run_game_loop(self):
        # Initialize players and scores
        player1 = Player("Player 1", "Spades")
        player2 = Player("Computer", "Hearts")
        player1.hand, player2.hand = deal_cards()
        player1_score = 0
        player2_score = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_game_board()
            # Sample usage of UI functions
            self.draw_player_hand(player1, 20, 100)
            self.draw_player_hand(player2, 20, SCREEN_HEIGHT - 200)
            self.draw_bid_input(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 100)
            self.draw_scores(player1_score, player2_score)

            self.update_screen()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

# Sample usage
if __name__ == "__main__":
    ui = UI()
    ui.run_game_loop()
