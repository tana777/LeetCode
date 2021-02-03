"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""

# Approach: BFS
# we need to know how many buildings are in this grid and if they are reachable, if one of them is not, then return -1
# We use numOfBuildingsCanReach to store the number of buildings can reach this current 0 empty space
# distOfBuildingsCanReach to store the cumulated distance of all the buildings can reach this current 0 empty space
# Every time we meet 1 (building), bfs from there, and fill in two matrices
# In the end, we loop over two matrices and find the point where all buildings can arrive plus with smallest distance

# Time Complexity: O(M^2*N^2)
# Space Complexity: O(M*N)

from typing import List 
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return -1
        nrow = len(grid)
        ncol = len(grid[0])
        
        numOfBuildingsCanReach = [[0]*ncol for i in range(nrow)]
        distOfBuildingsCanReach = [[0]*ncol for i in range(nrow)]
        dirUnit = [[0,1],[0,-1],[1,0],[-1,0]]
        numOfTotalBuildings = 0
        minDist = float('inf')
        
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == 1:
                    numOfTotalBuildings += 1
                    self.bfs(grid, row, col, nrow, ncol, dirUnit, numOfBuildingsCanReach, distOfBuildingsCanReach)
        

        for row in range(nrow):
            for col in range(ncol):
                if numOfBuildingsCanReach[row][col] == numOfTotalBuildings:
                    minDist = min(distOfBuildingsCanReach[row][col], minDist)
             
        if minDist == float('inf'):
            return -1
        return minDist
    
    def bfs(self, grid, row, col, nrow, ncol, dirUnit, numOfBuildingsCanReach, distOfBuildingsCanReach):
        queue = [(row,col)]
        visited = set()
        visited.add((row,col))
        level = 0

        while queue:
            level += 1
            num = len(queue)
            for i in range(num):
                curr = queue.pop(0)
                for step in dirUnit:
                    newRow = curr[0] + step[0]
                    newCol = curr[1] + step[1]
                    if not self.checkValid(grid, newRow, newCol, nrow, ncol, visited):
                        continue
                    queue.append((newRow,newCol))
                    visited.add((newRow, newCol))
                    numOfBuildingsCanReach[newRow][newCol] +=1
                    distOfBuildingsCanReach[newRow][newCol] += level
    
    def checkValid(self, grid, row, col, nrow, ncol, visited):
        if row < 0 or row >= nrow or col < 0 or col >= ncol:
            return False
        if (row,col) in visited:
            return False
        if grid[row][col] != 0:
            return False
        return True
        
                    
            
                    
                
        
        