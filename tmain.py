from tsettings import *
from sys import exit
from tetrisgame import Game
from tetrisscore import Score
from tetrispreview import Preview


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WWINDOW, HWINDOW))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tetris")

        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display_surface.fill(GRAY)
            self.game.run()
            self.score.run()
            self.preview.run()

            pygame.display.update()
            self.clock.tick(60)  # 60 fps


if __name__ == "__main__":
    main = Main()
    main.run()
