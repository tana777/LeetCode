"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
"""
# Approach: DFS backtrack
# notice how to check diagnoal attack
class Solution:
    def totalNQueens(self, n: int) -> int:
        total = []
        board = [["."]*n for i in range(n)]
        self.backtrack(total, board, n, 0)
        return len(total)
    
    def backtrack(self, total, board, n, row):
        if row == n:
            total.append(1)
            return
        
        for col in range(n):
            if not self.validCheck(board, row, col, n):
                continue
            board[row][col] = "Q"
            self.backtrack(total, board, n, row+1)
            board[row][col] = "."
            
    def validCheck(self, board, row, col, n):
        # check same column
        for r in range(n):
            if board[r][col] == 'Q':
                return False
            
        # check top left diagnoal attack
        srow, scol = row, col
        while srow >= 0 and srow < n and scol >= 0 and scol < n:
            if board[srow][scol] == 'Q':
                return False
            srow = srow-1
            scol = scol-1
        # check top right diagnoal attack
        srow, scol = row, col
        while srow >= 0 and srow < n and scol >= 0 and scol < n:
            if board[srow][scol] == 'Q':
                return False
            srow = srow-1
            scol = scol+1

        return True
        