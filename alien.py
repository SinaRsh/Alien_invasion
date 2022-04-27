import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the aliend and set the starting position."""
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set rect attributes.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #STart each new alien near the top ppf the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal location
        self.x = float(self.rect.x)