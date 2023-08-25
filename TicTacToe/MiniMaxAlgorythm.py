from Game import game

class MiniMax:

    def __init__(self, game:game) -> None:
        self.game = game
    
    def generateGameState(self) -> int:

        minScore = -20
        bestMove = 0

        for move in self.game.getBoard:

            if self.game.getBoard[move] not in ["X", "O"]:

                self.game.getBoard[move] = "X"
                maxScore = self.playGameState(False)
                self.game.getBoard[move] = str(move)

                if (maxScore > minScore):
                    minScore = maxScore
                    bestMove = move

        return bestMove

    def playGameState(self, computerMove:True|False) -> int:
        
        if self.game.checkWin("X"):
            return 10
        elif self.game.checkWin("O"):
            return -10
        elif self.game.checkDraw():
            return 0
        

        if computerMove:
            bestScore = -20
            
            for i in self.game.getBoard:
                if self.game.getBoard[i] not in ['O', 'X']:
                    self.game.getBoard[i] = 'X'
                    score = self.playGameState(False)
                    self.game.getBoard[i] = str(i)

                    if (score > bestScore):
                        bestScore = score
                    
            return bestScore
        else:
            bestScore = 20
            for i in self.game.getBoard:
                if self.game.getBoard[i] not in ['O', 'X']:
                    self.game.getBoard[i] = 'O'
                    score = self.playGameState(True)

                    self.game.getBoard[i] = str(i)
                    if (score < bestScore):
                        bestScore = score

            return bestScore