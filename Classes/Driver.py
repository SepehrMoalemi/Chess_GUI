# Purpose: Handle Game Flow
# %------------------------------------------ Packages -------------------------------------------% #
import pygame

from Classes import GUI
from Classes.Chess import Chess

# %---------------------------------------- Game Classes -----------------------------------------% #
class Game():
    def __init__(self, startPos : str, SETTINGS : GUI.Settings) -> None:
        # Make Board From Starting Position
        self.Chess = Chess(startPos)
        
        # Setup GUI
        self.Window = GUI.Window(SETTINGS)
        self.last_click = GUI.Coords()
        
    # %---------------------------------------- Methods --------------------------------------% #
    # Purpose: Run Game
    def Run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                match event.type:
                    # Stop Game
                    case pygame.QUIT:
                        running = False
                        
                    # Scale Board
                    case pygame.VIDEORESIZE:
                        self.Window.Resize(event)
                        
                    # Moving Pieces
                    case pygame.MOUSEBUTTONDOWN:
                        new_click = GUI.Coords(*pygame.mouse.get_pos())
            self.Window.RenderBoard(self.Chess.board)
            
    # Purpose: Select Piece to Move
    def SelectPiece(self, new_click : GUI.Coords) -> None:
        """
            If click is turn players piece:
            - #TODO Show Legal Moves [Optional]
            - #TODO Highlight Selected Piece 
            - #TODO Deselect if it has already been clicked
            
            If click is empty cell or opponent piece:
            - #TODO If Previous click is turn players piece
            - - #TODO Move piece to the selected square
            - - - #TODO Remove opponent piece if it was on that square
            - If this is the first click Do nothing
        """
        # Append if it's the first click
        if self.last_click.X == -1 and self.last_click.Y == -1:
            self.last_click = new_click
        else:
            # Check for double clicking same square
            if self.last_click == new_click:
                self.Window.DerenderSelectedPiece(new_click)
            else:
                # Move Piece to new square
                self.Window.RenderMove(self.Chess.board, self.last_click, new_click)
            # Reset Last Click
            self.last_click = GUI.Coords()