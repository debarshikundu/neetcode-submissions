class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(len(board)):
            if not self.isValidR(r,board):
                return False
        for c in range(len(board[0])):
            if not self.isValidC(c,board):
                return False
        for r in range(0,len(board),3):
            for c in range(0, len(board[0]), 3):
                if not self.isValidSquare(board,r,c):
                    return False
        return True
    def isValidR(self, r, board: List[List[str]]) -> bool:
        rSet = set()
        for c in range(len(board[0])):
            if board [r][c] == ".":
                continue
            if board[r][c] in rSet:
                return False
            rSet.add(board[r][c])
        return True
    def isValidC(self, c, board: List[List[str]]) -> bool:
        cSet = set()
        for r in range(len(board)):
            if board[r][c] == ".":
                continue
            if board[r][c] in cSet:
               return False
            cSet.add(board[r][c])
        return True
    def isValidSquare(self, board: List[List[str]],r, c) -> bool:
        sSet = set()
        for i in range(3):
            for j in range(3):
                if board[r+i][c+j] == ".":
                    continue 
                if board[r+i][c+j] in sSet:
                    return False
                sSet.add(board[r+i][c+j])
        return True



                
