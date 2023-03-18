# Purpose: Handle Piece Logic
# %------------------------------------------ Packages -------------------------------------------% #
from typing import NamedTuple

# %------------------------------------------- Structs -------------------------------------------% #
class Cell(NamedTuple):
    r : int = -1
    c : int = -1
    
# %----------------------------------------- Chess Classes ---------------------------------------------% #
class Chess():
    def __init__(self, startPos : str) -> None:
        self.startPos = startPos
        self.board    = self.makeBoard()
        self.move_log = []
        
    def __str__(self):
        # Printing Board State to terminal
        msg = ""
        
        # Add rows
        line = "  " + "+----" * 8 + "+"
        for n, row in enumerate(self.board):
            # Add row Coords
            msg += line + f'\n{n} '
            
            # Add cells
            for cell in row:
                msg += f'| {cell} '
                
            # Add cols
            msg += '|' + '\n'
        msg += line + '\n '
        
        # Add col Coords
        for i in range(65, 73):
            msg += f'    {chr(i)}'
        msg += " " + '\n'
        return msg
        
    # %---------------------------------------- Methods --------------------------------------% #
    # Purpose: Make Board
    def makeBoard(self, startPos = ""):
        """
        Board is a 2D List of 8x8
        Piece = (w, b)x(R,N,B,K,Q,P)
        ex) bR = black rook
            wP = white pawn
        """
        # Check if Position was Provided
        if startPos == "":
            startPos = self.startPos
            
        board = []
        emptySquare = ['  ']
        for s in startPos.split('/'):
            row = []
            for c in s:
                # Finished Board
                if c == ' ':
                    break
                
                # Empty Squares ascii 49-56 <-> int 1-8
                elif 48<ord(c) and ord(c)<57:
                    row.extend(emptySquare * int(c))
                    
                # Store the Black Pieces
                elif c.islower():
                    row.append('b' + c.upper())
                
                # Store the White Pieces   
                elif c.isupper():
                    row.append('w' + c)
            board.append(row)
        return board

    # TODO Purpose: Move Piece
    def MovePiece(self, cell_start, cell_end) -> None:
        pass
    
# Todo: 
# - makeBoard: Implement w KQkq - 0 1 part of FEN