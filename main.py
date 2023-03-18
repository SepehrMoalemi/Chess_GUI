# Purpose: Driver File
# %------------------------------------------ Packages -------------------------------------------% #
from Classes import GUI
from Classes import Chess
from Classes.Driver import Game

# %------------------------------------------ Functions ------------------------------------------% #
def testing():
        pos1 = [1, 3]
        pos2 = [1,3]
        coord1 = GUI.Coords(*pos1)
        coord2 = GUI.Coords(*pos2)
        print(coord1 == coord2)
    # pass

# %-------------------------------------------- Main ---------------------------------------------% #
def main():
    # Set Starting Position
    startPos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    
    # Set GUI Settings
    DIM       = 8                               # Board of (DIM X DIM)
    LENGTH    = 512                             # Height and Width of the Board
    CELL_SIZE = LENGTH//DIM      
    MAX_FPS   = 16
    
    # Set GUI Theme
    BOARD_THEMES = {"Brown" : [(240, 217, 181), (181, 136, 99)],
                    "Green" : [(255, 255, 221),(134, 166, 102)]}
    
    PIECE_THEME = "Cardinal"
    BOARD_THEME = BOARD_THEMES['Brown']          
    
    # Build GUI Settings
    THEME    = GUI.Themes(PIECE_THEME, BOARD_THEME)
    SETTINGS = GUI.Settings(DIM=DIM,
                            LENGTH=LENGTH,
                            CELL_SIZE=CELL_SIZE,
                            MAX_FPS=MAX_FPS,
                            THEME=THEME)

    # Run Game
    game = Game(startPos, SETTINGS)
    game.Run()
    
    # ? ---- Testing ----- ? #
    # testing()
# %--------------------------------------------- Run ---------------------------------------------% #
if __name__ == '__main__':
    print(f'{"Start":-^{50}}')
    main()
    print(f'{"End":-^{50}}')
    
    # Todo: 
    # Resiable Window?
    # - Issue with immutable type