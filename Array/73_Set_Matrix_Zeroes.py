"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

## Approach 1: Use O(m+n) space to store the row and col of zero elements
"""
Time Complexity: O(m*n)
Space Complexity: O(m+n) m: number of row n:number of column
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        recordRow = set()
        recordCol = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    recordRow.add(i)
                    recordCol.add(j)
        self.updateZeroes(matrix, recordRow, recordCol, m, n)
        return matrix 
    
    def updateZeroes(self, matrix, recordRow, recordCol, m, n):
        for i in recordRow:
            matrix[i][:] = [0 for i in range(n)]
        for j in recordCol:
            for rowindex in range(m):
                matrix[rowindex][j] = 0


## Approach 2: Use constant space
"""
Time Complexity: O(m*n)
Space Complexity: O(1)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 0->0  -- 0
        # else->0 -- '0'
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.updateMatrix(matrix, i, j, m, n)
        self.restoreZeroes(matrix, m, n)
        
    def updateMatrix(self, matrix, rowX, colY, m, n):
        for col in range(n):
            if matrix[rowX][col] != 0:
                matrix[rowX][col] = '0'
        for row in range(m):
            if matrix[row][colY] != 0:
                matrix[row][colY] = '0'
    
    def restoreZeroes(self, matrix, m, n):
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
        
        
        
