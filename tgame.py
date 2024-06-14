from tsettings import *


class Game:
    def __init__(self):
        self.surface = pygame.Surface((WGAME, HGAME))
        self.display_surface = pygame.display.get_surface()
        self.rect = self.surface.get_rect(topleft=(PADDING, PADDING))

        self.line_surface = self.surface.copy()
        self.line_surface.fill((0, 255, 0))
        self.line_surface.set_colorkey((0, 255, 0))
        self.line_surface.set_alpha(120)

    def add_grid(self):
        for col in range(1, COLS):
            x = col * CELL_SIZE
            pygame.draw.line(self.surface, LINE_COLOUR, (x, 0), (x, self.surface.get_height()), 1)

        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.surface, LINE_COLOUR, (0, y), (self.surface.get_width(), y), 1)

        self.surface.blit(self.line_surface, (0, 0))

    def run(self):
        self.surface.fill(GRAY)

        self.add_grid()
        self.display_surface.blit(self.surface, (PADDING, PADDING))  # block in its transfer
        pygame.draw.rect(self.display_surface, LINE_COLOUR, self.rect, 2, 2)

