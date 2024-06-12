from tetrissettings import *


class Score:
    def __init__(self):
        self.surface = pygame.Surface((WSBAR, HGAME * SCORE_HEIGHT_FRACTION - PADDING))
        self.rect = self.surface.get_rect(
            bottomright=(WWINDOW - PADDING, HWINDOW - PADDING)
        )
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)
