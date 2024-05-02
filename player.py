import pygame

class Player:
    def __init__(self, name, assigned_suit, position):
        self.name = name
        self.assigned_suit = assigned_suit
        self.hand = []
        self.bids = []
        self.score = 0
        self.position = position

    def draw_hand(self, screen):
        for i, card in enumerate(self.hand):
            card.position = pygame.Rect(self.position[0] + i * 50, self.position[1], 60, 90)
            card.draw(screen)

    def update_hand(self, new_hand):
        self.hand = new_hand

    def reset_bids(self):
        self.bids = []

    def add_score(self, points):
        self.score += points
