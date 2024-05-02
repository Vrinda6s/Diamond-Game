import pygame
import sys

class EventsHandler:
    def __init__(self, ui, game_logic):
        self.ui = ui
        self.game_logic = game_logic

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event)

    def handle_mouse_click(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.ui.bid_input_rect.collidepoint(mouse_pos):
            self.process_bid_input()

    def process_bid_input(self):
        # Placeholder for processing bid input
        print("Processing bid input...")

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def start_new_round(self):
        self.game_logic.start_new_round()
        # Additional logic for UI updates or actions related to starting a new round

    def end_game(self):
        self.game_logic.check_game_over()
        # Additional logic for UI updates or actions related to ending the game
