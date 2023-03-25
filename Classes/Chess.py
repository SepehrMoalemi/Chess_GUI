# Purpose: Handle Piece Logic
# %------------------------------------------ Packages -------------------------------------------% #
from typing import NamedTuple

# %------------------------------------------- Structs -------------------------------------------% #
class Cell(NamedTuple):
    r : int = -1
    c : int = -1
    
# %----------------------------------------- Chess Classes ---------------------------------------% #
class Chess():
    def __init__(self, START_POS_FEN : str) -> None:
        self.START_POS_FEN = START_POS_FEN

        self.move_log = []                  # Store Moves to Go back to
        self.EMPTY_CELL = '  '              # Place Holder for an empty cell in 2D board list
        
        self.board = self.fen2board()
        
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
    def fen2board(self, START_POS_FEN = "") -> list[list[str]]:
        """
        Board is a 2D List of 8x8
        Piece = (w, b)x(R,N,B,K,Q,P)
        ex) bR = black rook
            wP = white pawn
        """
        # Check if Position was Provided
        if START_POS_FEN == "":
            START_POS_FEN = self.START_POS_FEN
            
        board = []
        for s in START_POS_FEN.split('/'):
            row = []
            for c in s:
                # Finished Board
                if c == ' ':
                    break
                
                # Empty Squares ascii 49-56 <-> int 1-8
                elif 48<ord(c) and ord(c)<57:
                    row.extend([self.EMPTY_CELL] * int(c))
                    
                # Store the Black Pieces
                elif c.islower():
                    row.append('b' + c.upper())
                
                # Store the White Pieces   
                elif c.isupper():
                    row.append('w' + c)
            board.append(row)
        return board

    # Purpose: Move Piece
    def move_piece(self, cell_start : Cell, cell_end : Cell) -> None:
        # Check if it is a repeated cell
        if cell_start == cell_end:
            return
        
        piece = self.get_piece(cell_start)
        
        # Check if destination is empty
        if self.get_piece(cell_end) == self.EMPTY_CELL:
            self.set_piece(piece, cell_end)
            # TODO If statement for castling, promoting, enpassant
        
        # Take Opponent Piece
        else:
            self.set_piece(piece, cell_end)
            # TODO add chess notation
            
        # Set starting cell to empty since we moved
        self.set_piece(self.EMPTY_CELL, cell_start)
    
    # TODO Purpose: Convert to Chess Notation
    def move2notation(self, cell_start : Cell, cell_end : Cell) -> str:
        return ""
    
    # Purpose: Get Piece from cell
    def get_piece(self, cell : Cell) -> str:
        return self.board[cell.r][cell.c]
    
    # Purpose: Put Piece in cell
    def set_piece(self, piece : str, cell : Cell) -> None:
        self.board[cell.r][cell.c] = piece
    
    # Purpose: Check if square is empty
    def cell_isEmpty(self, cell : Cell) -> bool:
        return self.get_piece(cell) == self.EMPTY_CELL
# Todo: 
# - makeBoard: Implement w KQkq - 0 1 part of FEN
# - move_piece: castle, enpassant, promote