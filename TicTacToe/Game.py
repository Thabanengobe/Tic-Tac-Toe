
class game:

    def __init__(self, board : dict) -> None:
        self.board = board 
        self.winingMoves = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 5, 9], [3, 5, 7], [2, 5, 8],
            [1, 4, 7], [3, 6, 9]
        ]

    def checkWin(self, symbol:str) -> True|False:

        for i in self.winingMoves:
            if self.board[i[0]] == self.board[i[1]] and self.board[i[1]] == self.board[i[2]] and self.board[i[2]] == symbol:
                return True


    def checkDraw(self) -> True|False:
        
        for move in self.board:
            if self.board[move] not in ["O", "X"]:
                return False

    def isgameOver(self, symbol:str):
        
        if self.checkWin(symbol): return symbol+" Wins"
        elif self.checkDraw(): return "Draw!!"      

    def updateGameBoard(self, move: int, symbol: str):
        self.board[move] = symbol

    @property
    def getBoard(self) -> dict:
        return self.board
    

    def showGameBoard(self) -> None:

        for sqaure in self.board.keys():

            if sqaure == 4 or sqaure == 7: print()

            print(end=f"\t  {self.board[sqaure]}")

            if sqaure != 3 and sqaure != 6 and sqaure != 9: print(end="   |")

            if sqaure == 3 or sqaure == 6:
                print(end="\n\t------+------+-------")
        print()