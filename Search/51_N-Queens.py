"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""

# Approach: DFS backtrack

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for i in range(n)]
        res = []
        self.backtrack(res, board, n, 0)
        return res
    
    def backtrack(self, res, board, n, row):
        if row == n:
            res.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if not self.checkValid(board, row, col, n):
                continue
            board[row][col] = "Q"
            self.backtrack(res, board, n, row+1)
            board[row][col] = "."
    
    
    def checkValid(self, board, row, col, n):
        # check same column attack
        for r in range(n):
            if board[r][col] == "Q":
                return False
            
        # check top left diagnoal attack
        srow, scol = row, col
        while srow-1 >= 0 and srow < n and scol-1 >= 0 and scol < n:
            srow = srow-1
            scol = scol-1
            if board[srow][scol] == 'Q':
                return False
        # check top right diagnoal attack
        srow, scol = row, col
        while srow-1 >= 0 and srow < n and scol >= 0 and scol < n-1:
            srow = srow-1
            scol = scol+1
            if board[srow][scol] == 'Q':
                return False

        return True