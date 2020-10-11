"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
###### Note: we cannot update the status one by one and then use the updated status to compute other cells state,
######       this is not simultaneously change.

## Approach 1: Use additional space
"""
Time Complexity: O(m*n)
Space Complexity: O(m*n)

1. create a copy of board
2. iterate over the copy board, for each cell, go over its 8 neighbors to compute total count of live neighbors
3. update the status in board according to its current state and count of live nighbors based on rules
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])
        neighbors = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
        ## copy board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
        ## iterate over the original board
        ## for each cell, check its count of live neighbors
        ## update its own status accordingly
        for i in range(rows):
            for j in range(cols):
                countofLives = self.calculateCountofLives(copy_board, i, j, rows, cols, neighbors)
                self.updateCellStatus(board, i, j, countofLives, copy_board)
        
        
    def calculateCountofLives(self, copy_board, rowX, colY, rows, cols, neighbors):
        countofLives = 0
        for neighbor in neighbors:
            n_x = rowX + neighbor[0]
            n_y = colY + neighbor[1]
            if n_x >= 0 and n_x < rows and n_y >= 0 and n_y < cols:
                if copy_board[n_x][n_y] == 1:
                    countofLives += 1
        return countofLives
    
    def updateCellStatus(self, board, rowX, colY, countofLives, copy_board):
        if copy_board[rowX][colY] == 1:
            if countofLives < 2 or countofLives > 3:
                board[rowX][colY] = 0
        else:
            if countofLives == 3:
                board[rowX][colY] = 1
                
            
## Approach 2: improve with constant space
"""
Time Complexity: O(m*n)
Space Complexity: O(1)

1. set up two labels to record the status change
0->1 death to alive 2
1->0 alive to death -1
2. iterate over the board, for each cell, compute count of live neighbors
3. using lables we set up before to update its status with count of live neighbors and current state
4. go through the board again and recover its real state
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        neighbors = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
        # 0->1 death to alive 2
        # 1->0 alive to death -1
        for i in range(rows):
            for j in range(cols):
                countOfLives = self.calculateLiveNeighbors(board,i,j,rows,cols,neighbors)
                self.updateCellStatus(board,i,j,countOfLives)
        self.recoverRealStatus(board, rows, cols)
    
    def calculateLiveNeighbors(self,board,rowX,colY,rows,cols,neighbors):
        countOfLives = 0
        for neighbor in neighbors:
            nx = rowX + neighbor[0]
            ny = colY + neighbor[1]
            if nx>=0 and nx<rows and ny>=0 and ny<cols:
                if abs(board[nx][ny]) == 1:
                    countOfLives += 1
        return countOfLives
    
    def updateCellStatus(self,board,rowX,colY,countOfLives):
        if board[rowX][colY] == 1:
            if countOfLives < 2 or countOfLives > 3:
                board[rowX][colY] = -1
        else:
            if countOfLives == 3:
                board[rowX][colY] = 2
    
    def recoverRealStatus(self,board,rows,cols):
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
                    
## follow up: what if the board is infinity?
"""
- not possible to iterate a matrix that large
- not able to fit entire matrix in memory (store the matrix row by row)
- waste of space if most of the cell are all dead

Solution: only store the position of live cells

live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
"""     
                
      
        
                
        
        