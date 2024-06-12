import pygame

COLS = 10
ROWS = 20
CELL_SIZE = 40
WGAME, HGAME = COLS * CELL_SIZE, ROWS * CELL_SIZE

WSBAR = 200
PREVIEW_HEIGHT_FRACTION = 0.7
SCORE_HEIGHT_FRACTION = 1 - PREVIEW_HEIGHT_FRACTION

PADDING = 20
WWINDOW = WGAME + WSBAR + PADDING * 3
HWINDOW = HGAME + PADDING * 2

UP_START_SPEED = 800
MOVE_WAIT_TIME = 200
ROTATE_WAIT_TIME = 200
BLOCK_OFFSET = pygame.Vector2((COLS // 2, -1))

YELLOW = "#f1e60d"
RED = "#e51b20"
BLUE = "#204b9b"
GREEN = "#65b32e"
PURPLE = "#7b217f"
CYAN = "6cc6d9"
ORANGE = "f07e13"
GRAY = "#1C1C1C"
LINE_COLOUR = "#FFFFFF"

SHAPES = {
    "T": {"shape": [(0, 0), (-1, 0), (1, 0), (0, -1)], "colour": PURPLE},
    "J": {"shape": [(0, 0), (-1, 0), (0, -1), (0, -2)], "colour": YELLOW},
    "L": {"shape": [(0, 0), (1, 0), (0, -1), (0, -2)], "colour": BLUE},
    "Z": {"shape": [(0, 0), (-1, 0), (0, -1), (1, -1)], "colour": ORANGE},
    "S": {"shape": [(0, 0), (-1, -1), (0, -1), (1, 0)], "colour": CYAN},
    "I": {"shape": [(0, 0), (0, -1), (0, -2), (0, -3)], "colour": GREEN},
    "O": {"shape": [(0, 0), (0, -1), (-1, 0), (-1, -1)], "colour": RED},
}

SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}
