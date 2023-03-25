# Purpose: Handle GUI
# %------------------------------------------ Packages -------------------------------------------% #
import pygame
from Classes import Chess
from typing  import NamedTuple

# %------------------------------------------- Structs -------------------------------------------% #
class Coords(NamedTuple):
    X : int = -1
    Y : int = -1
    
class Themes(NamedTuple):
    PIECE : str
    BOARD : list
    
class Settings(NamedTuple):
    DIM       : int
    LENGTH    : int
    CELL_SIZE : int  
    MAX_FPS   : int
    THEME     : Themes

# %------------------------------------------ GUI Classes ----------------------------------------% #
class Window():
    def __init__(self, SETTINGS : Settings) -> None:
        self.SETTINGS = SETTINGS 
        self.IMAGES = {}
        self.PIECES = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wP', 
                       'bR', 'bN', 'bB', 'bQ', 'bK', 'bP']
        
        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption("Jeff The Engine")
        
        # Setup Screen
        self.screen = pygame.display.set_mode((self.SETTINGS.LENGTH,
                                               self.SETTINGS.LENGTH),
                                               pygame.RESIZABLE)
        # Setup Clock
        self.clock  = pygame.time.Clock()
        
        # Load Pieces From Image Folder
        self.load_piece_from_file()
        
    # %---------------------------------------- Reneder Methods --------------------------------------% #
    # Purpose: Render Window
    def render_window(self) -> None:
        self.clock.tick(self.SETTINGS.MAX_FPS)
        pygame.display.update()
        
    # Purpose: Render the Entire Board + Pieces
    def render_board(self, board : list[list[str]]) -> None:
        self.render_background()
        self.render_pieces(board)
        self.render_window()

    # Purpose: Render Board
    def render_background(self) -> None:
        cs = self.SETTINGS.CELL_SIZE
        for r in range(self.SETTINGS.DIM):
            for c in range(self.SETTINGS.DIM):
                color = self.SETTINGS.THEME.BOARD[(r + c)%2]
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(c * cs, r * cs, 
                                                 cs,     cs))
    # Purpose: Render Pieces
    def render_pieces(self, board : list[list[str]]) -> None:
        cs = self.SETTINGS.CELL_SIZE
        for r in range(self.SETTINGS.DIM):
            for c in range(self.SETTINGS.DIM):
                # Get piece
                piece = board[r][c]
                
                # Check for Empty Square
                if piece != '  ':
                    self.screen.blit(self.IMAGES[piece],
                                     pygame.Rect(c * cs, r * cs, 
                                                     cs,     cs))
    
    # Purpose: Render Piece Moving by start->end click
    def render_move(self, chess : Chess.Chess, pos_start : Coords, pos_end : Coords) -> None:
        # Convert Coords to Cell position
        cell_start = self.coord2cell(pos_start)
        cell_end   = self.coord2cell(pos_end)
        
        # Move Piece
        chess.move_piece(cell_start, cell_end)
        
    # TODO Purpose: Derender Selected Piece
    def DerenderSelectedPiece(self, pos : Coords) -> None:
        print(self.coord2cell(pos))
        
    # %---------------------------------------- Board Methods --------------------------------------% #
    # Purpose: resize Window based on User Event
    def resize(self, event) -> None:
        self.screen = pygame.display.set_mode((event.w, event.h),
                                               pygame.RESIZABLE)
    
    # %---------------------------------------- Helper Methods --------------------------------------% #
    # Purpose: Load PNG Pieces
    def load_piece_from_file(self) -> None:
        for piece in self.PIECES:
            path = f'Images/{self.SETTINGS.THEME.PIECE}_Theme/'
            
            # Load and Smooth Scale the images
            img = pygame.image.load(path + piece + ".png")
            img = pygame.transform.smoothscale(img, (self.SETTINGS.CELL_SIZE, 
                                                     self.SETTINGS.CELL_SIZE))
            self.IMAGES[piece] = img
            
    # Purpose: Cursor Coordinates to Cell Position
    def coord2cell(self, coord : Coords) -> Chess.Cell:
        c = coord.X // self.SETTINGS.CELL_SIZE
        r = coord.Y // self.SETTINGS.CELL_SIZE
        return Chess.Cell(r,c)