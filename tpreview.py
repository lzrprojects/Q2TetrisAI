from tsettings import *


class Preview:
    def __init__(self):
        self.surface = pygame.Surface((WSBAR, HGAME * PREVIEW_HEIGHT_FRACTION))
        self.rect = self.surface.get_rect(topright=(WWINDOW - PADDING, PADDING))
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)
