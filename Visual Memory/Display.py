from Data import Game_Board
import pygame
import sys
import time



# Constants
WIDTH, HEIGHT = 520, 520
ROWS, COLS = 7, 7
GRID_SIZE = WIDTH//ROWS
BLACK = (33, 33, 33)
WHITE = (51, 51, 51)
CLICKED_COLOR_RIGHT = (200, 200, 0)
CLICKED_COLOR_WRONG = (50, 50, 50)
GAME_STATS = False
MOUSE_BUTTON_LEFT_STATE = False
FPS = 60
SQURENUM = 17
FLASHTIMER = 2



# Create the chessboard
DisplayBoard = []
BackBoard = []



Mistakes = 0
Score = 0


def display(directory, coordinate, size):
    image = pygame.image.load(directory)
    resized_image = pygame.transform.scale(image, (size, size))
    Screen.blit(resized_image, coordinate)

def ResizableWindow():
    global WIDTH, HEIGHT, ROWS, COLS, GRID_SIZE,Screen
    if (WIDTH, HEIGHT) != Screen.get_size() or HEIGHT % GRID_SIZE != 0:
        Screen.fill((0, 0, 0))
        WIDTH, HEIGHT = Screen.get_size()
        if WIDTH >= HEIGHT:
            GRID_SIZE = HEIGHT//ROWS
            WIDTH, HEIGHT = GRID_SIZE*ROWS, GRID_SIZE*COLS
            pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        else:
            GRID_SIZE = WIDTH//ROWS
            WIDTH, HEIGHT = GRID_SIZE * ROWS, GRID_SIZE*COLS
            pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)


#convert mouse postion to board squere
def get_square_from_cursor(pos):
    col = pos[0] // GRID_SIZE
    row = pos[1] // GRID_SIZE
    return row, col


def ClickSqure(event,mouse_squre):
    global MOUSE_BUTTON_LEFT_STATE, DisplayBoard, Board_Checker_Once_2, Mistakes, Score
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and Board_Checker_Once_2 == True:  #Left mouse button clicked
            MOUSE_BUTTON_LEFT_STATE = True

        
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1 and Board_Checker_Once_2 == True:  # Left mouse button released
            MOUSE_BUTTON_LEFT_STATE = False
            if mouse_squre[0] in range(0, ROWS) and mouse_squre[1] in range(0, COLS):
                if DisplayBoard[mouse_squre[0]][mouse_squre[1]] == 0:
                    DisplayBoard[mouse_squre[0]][mouse_squre[1]] = 2
                    Mistakes += 1

                if DisplayBoard[mouse_squre[0]][mouse_squre[1]] == 5:
                    DisplayBoard[mouse_squre[0]][mouse_squre[1]] = 6
                    Score += 1
    #for row in range(ROWS):
        #for col in range(COLS):
            #if DisplayBoard[row][col] == 3:
                #DisplayBoard[row][col] = 0 if (row + col) % 2 == 0 else 1
    
    if MOUSE_BUTTON_LEFT_STATE == True:
        pass


BoardSetting = None
def SetBackBoard():
    global ROWS, COLS, BackBoard,BoardSetting ,SQURENUM
    Board = Game_Board()
    Board.ROWS, Board.COLS = ROWS, COLS
    Board.TestSqureNum = SQURENUM
    Board.GenerateBoard()
    Board.FillBoard()
    BackBoard = Board.Board
    BoardSetting = Board


Board_Checker_Once_1 = False
Board_Checker_Once_2 = False
Timer = 0
def Board_Checker():
    global BackBoard, DisplayBoard, Board_Checker_Once_1, Board_Checker_Once_2, BoardSetting, FLASHTIMER, Mistakes, Score, Timer
    if Board_Checker_Once_1 == False:
        SetBackBoard()
        for cor in BoardSetting.PickedSqures:
            DisplayBoard[cor[0]][cor[1]] = 4
            Board_Checker_Once_1 = True
        Timer = time.time() + FLASHTIMER

    if Timer <= time.time() and Board_Checker_Once_2 == False:
        for cor in BoardSetting.PickedSqures:
            DisplayBoard[cor[0]][cor[1]] = 5
            Board_Checker_Once_2 = True
    

    # reset game
    if Mistakes >= 3 or Score/BoardSetting.TestSqureNum == 1:
        DisplayBoard = [[0 for i in range(COLS)] for j in range(ROWS)]
        Board_Checker_Once_1 = False
        Board_Checker_Once_2 = False
        print(f"{Score}/{BoardSetting.TestSqureNum}")
        Mistakes = 0
        Score = 0
    




#Start the window
def InitializeWindow():
    global WIDTH, HEIGHT, GAME_STATS, Screen, DisplayBoard
    pygame.init()
    Screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Visual Memory")
    DisplayBoard = [[0 for i in range(COLS)] for j in range(ROWS)]
    GAME_STATS = True



# Main game loop
def MainWindowLoop():
    global WIDTH, HEIGHT, ROWS, COLS, GRID_SIZE, GAME_STATS, FPS, Screen,DisplayBoard
    while True:
        time.sleep(1/FPS)
        # Get cursor position
        mouse_pos = pygame.mouse.get_pos()
        mouse_squre= get_square_from_cursor(mouse_pos)


        for event in pygame.event.get():
            #Constant Event functions
            ClickSqure(event,mouse_squre)
            if event.type == pygame.QUIT:
                GAME_STATS = False
                pygame.quit()
                sys.exit()

        #Draw the board
        for row in range(ROWS):
            for col in range(COLS):
                color = WHITE if DisplayBoard[row][col] == 0 else BLACK
                if DisplayBoard[row][col] == 0:
                    color = BLACK

                if DisplayBoard[row][col] == 1:
                    color = WHITE

                if DisplayBoard[row][col] == 2:
                    color = tuple(int(value * 0.5) for value in color)
                
                if DisplayBoard[row][col] == 3:
                    color = tuple(int(value * 0.8) for value in color)

                if DisplayBoard[row][col] == 4:
                    color = (37, 115, 193)

                if DisplayBoard[row][col] == 5:
                    color = BLACK
                    
                if DisplayBoard[row][col] == 6:
                    color = (0,255,0)

                pygame.draw.rect(Screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        for row in range(ROWS):
            pygame.draw.line(Screen, (0,0,0), (row* GRID_SIZE, 0) ,(row* GRID_SIZE, HEIGHT), 3)
        for col in range(COLS):
            pygame.draw.line(Screen, (0,0,0), (0, col* GRID_SIZE) ,(WIDTH, col* GRID_SIZE), 3)

        

        #Constantnt Functions
        ResizableWindow()
        Board_Checker()
        #===========
        pygame.display.update()