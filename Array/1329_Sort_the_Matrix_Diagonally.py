"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 
Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

"""

"""
Time Complexity: O(m*n)
Space Complexity: O(min(m,n))
"""
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        for col in range(cols):
            sortedLs = self.sortList(mat, 0, col, rows, cols)
            self.updateDiagonal(mat, 0, col, sortedLs)
        for row in range(1, rows):
            sortedLs = self.sortList(mat, row, 0, rows, cols)
            self.updateDiagonal(mat, row, 0, sortedLs)
        return mat
    
    def sortList(self, mat, rowX, colY, rows, cols):
        res = []
        for l in range(min(rows, cols)):
            nx = rowX + l*1
            ny = colY + l*1
            if nx >= 0 and nx < rows and ny >= 0 and ny < cols:
                res.append(mat[nx][ny])
        return sorted(res)
    
    def updateDiagonal(self, mat, rowX, colY, sortedLs):
        for l in range(len(sortedLs)):
            mat[rowX + l*1][colY + l*1] = sortedLs[l]


    
## Approach 2: Use hint 
# All cells in the same diagonal (i,j) have the same difference so we can get the diagonal of a cell using the difference i-j.
"""
1. use a dictionary to store diagnoal value with corresponding key = i-j
2. sort the diagnoal list
3. restore the matrix
"""
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        diagnoalDict = {}
        for i in range(rows):
            for j in range(cols):
                if (i-j) in diagnoalDict:
                    diagnoalDict[i-j].append(mat[i][j])
                else:
                    diagnoalDict[i-j] = [mat[i][j]]
                    
        for key in diagnoalDict:
            diagnoalDict[key] = sorted(diagnoalDict[key])
        
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = diagnoalDict[i-j].pop(0)
        return mat
        
        
