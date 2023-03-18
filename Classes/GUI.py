# Purpose: Handle GUI
# %------------------------------------------ Packages -------------------------------------------% #
import pygame
from typing import NamedTuple

from Classes.Chess import Chess

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
        self.LoadPieces()
        
    # %---------------------------------------- Methods --------------------------------------% #
    # Purpose: Render Window
    def RenderBoard(self, board : list) -> None:
        self.RenderBackground()
        self.RenderPieces(board)
        self.clock.tick(self.SETTINGS.MAX_FPS)
        pygame.display.update()
    
    # Purpose: Render Board
    def RenderBackground(self) -> None:
        cs = self.SETTINGS.CELL_SIZE
        for r in range(self.SETTINGS.DIM):
            for c in range(self.SETTINGS.DIM):
                color = self.SETTINGS.THEME.BOARD[(r + c)%2]
                pygame.draw.rect(self.screen, color,
                                 pygame.Rect(c * cs, r * cs, 
                                                 cs,     cs))
    # Purpose: Render Pieces
    def RenderPieces(self, board : list) -> None:
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
    # TODO Purpose: Derender Selected Piece
    def DerenderSelectedPiece(self, pos : Coords) -> None:
        pass
    
    # TODO Purpose: Render Piece Moving by start->end click
    def RenderMove(self, board : list, pos_start : Coords, pos_end : Coords) -> None:
        pass
        
    # Purpose: Resize Window based on User Event
    def Resize(self, event) -> None:
        self.screen = pygame.display.set_mode((event.w, event.h),
                                               pygame.RESIZABLE)
                    
    # Purpose: Load PNG Pieces
    def LoadPieces(self) -> None:
        for piece in self.PIECES:
            path = f'Images/{self.SETTINGS.THEME.PIECE}_Theme/'
            
            # Load and Smooth Scale the images
            img = pygame.image.load(path + piece + ".png")
            img = pygame.transform.smoothscale(img, (self.SETTINGS.CELL_SIZE, 
                                                     self.SETTINGS.CELL_SIZE))
            self.IMAGES[piece] = img
       
    