import pygame

class Card:
    def __init__(self, suit, value, position):
        self.suit = suit
        self.value = value
        self.position = position
        self.is_selected = False

    def draw(self, screen):
        card_color = (255, 255, 255)
        if self.is_selected:
            card_color = (200, 200, 200)  # Highlight selected card
        pygame.draw.rect(screen, card_color, self.position)
        pygame.draw.rect(screen, (0, 0, 0), self.position, 2)
        font = pygame.font.Font(None, 24)
        text = font.render(f"{self.value} {self.suit}", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.position.center)
        screen.blit(text, text_rect)

    def flip(self):
        self.is_selected = not self.is_selected
