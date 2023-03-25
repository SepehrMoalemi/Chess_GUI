# Purpose: Handle Game Flow
# %------------------------------------------ Packages -------------------------------------------% #
import pygame

from Classes import GUI
from Classes.Chess import Chess

# %---------------------------------------- Game Classes -----------------------------------------% #
class Game():
    def __init__(self, START_POS_FEN : str, SETTINGS : GUI.Settings) -> None:
        # Make Board From Starting Position
        self.Chess = Chess(START_POS_FEN)
        
        # Setup GUI
        self.Window = GUI.Window(SETTINGS)
        self.last_click = GUI.Coords()
        
    # %---------------------------------------- Methods --------------------------------------% #
    # Purpose: run Game
    def run(self) -> None:
        running = True
        # self.Window.RenderBoard(self.Chess.board)
        while running:
            for event in pygame.event.get():
                match event.type:
                    # Stop Game
                    case pygame.QUIT:
                        running = False
                        
                    # Scale Board
                    case pygame.VIDEORESIZE:
                        self.Window.resize(event)
                        
                    # Moving Pieces
                    case pygame.MOUSEBUTTONDOWN:
                        new_click = GUI.Coords(*pygame.mouse.get_pos())
                        self.move_with_click(new_click)
            # self.Window.RenderWindow()
            self.Window.render_board(self.Chess.board)
            
    # Purpose: Select Piece to Move
    def move_with_click(self, new_click : GUI.Coords) -> None:
        """
            If click is turn players piece:
            - #TODO Show Legal Moves [Optional]
            - #TODO Highlight Selected Piece 
            - Deselect if it has already been clicked
            
            If click is empty cell or opponent piece:
            - #TODO If Previous click is turn players piece
            - - # Move piece to the selected square
            - - - # Remove opponent piece if it was on that square
            - If this is the first click Do nothing
        """
            
        # Check if this is the first click
        if self.isFirstClick():
            # Do nothing if clicked on empty square
            if self.Chess.cell_isEmpty(self.Window.coord2cell(new_click)):
                return
            
            self.last_click = new_click
        
        else:
            # Check for double clicking same square
            if self.last_click == new_click:
                print("Double Clicking!")
                self.Window.DerenderSelectedPiece(new_click) 
                
            else:
                # Move Piece to new square
                self.Window.render_move(self.Chess, self.last_click, new_click) 
                
            # Reset Last Click
            self.last_click = GUI.Coords()
        
    # Purpose: Check if it's the first click
    def isFirstClick(self) -> bool:
        return self.last_click.X == -1 and self.last_click.Y == -1