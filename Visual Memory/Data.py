import random

class Game_Board:
    def __init__(self):
        self.ROWS = 0
        self.COLS = 0
        self.TestSqureNum = 0
        self.Board = []
        self.PickedSqures = []

    def GenerateBoard(self):
        self.Board = [[0 for i in range(self.COLS)] for j in range(self.ROWS)]


    def FillBoard(self):
        PickedSqures = []
        for i in range (0,self.TestSqureNum):
            Squre = random.randint(0,self.ROWS - 1) , random.randint(0,self.COLS - 1)
            while Squre in PickedSqures:
                Squre = random.randint(0,self.ROWS - 1) , random.randint(0,self.ROWS - 1)
            PickedSqures.append(Squre)
        
        self.PickedSqures = PickedSqures

        for Squre in PickedSqures:
            self.Board[Squre[0]][Squre[1]] = 4
