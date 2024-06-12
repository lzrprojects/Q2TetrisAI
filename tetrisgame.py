from Tsettings import *


class Game:
    def __init__(self):
        self.surface = pygame.Surface((WGAME, HGAME))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(
            self.surface, (PADDING, PADDING)
        )  # block in its transfer
