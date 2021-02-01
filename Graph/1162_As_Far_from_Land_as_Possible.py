"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""


## Approach 1 Probably most intuitive method but TLE
# Iterate over the grid, if we meet water, then bfs from this point, and return the closet land to it
# compute the distance and compare with the maximum distance so far
# Time compleixty: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        maxDistance = -1
        leng = len(grid)
        for row in range(leng):
            for col in range(leng):
                if grid[row][col] == 0:
                    land = self.bfs(grid, row, col, leng)
                    if land:
                        maxDistance = max(maxDistance, abs(land[0]-row) + abs(land[1]-col))
        return maxDistance
        
    
    def bfs(self, grid, row, col, leng):
        queue = [(row,col)]
        unit = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        while queue:
            n = len(queue)
            for i in range(n):
                ele = queue.pop(0)
                visited.add(ele)
                if grid[ele[0]][ele[1]] == 1:
                    return [ele[0],ele[1]]
                
                for step in unit:
                    nrow = ele[0] + step[0]
                    ncol = ele[1] + step[1]
                    if nrow >=0 and nrow < leng and ncol >= 0 and ncol < leng and (nrow,ncol) not in visited:
                        queue.append((nrow,ncol))
                        

## Approach 2: alter the lens, let's start from land instead of water
## Iterate over the grid and put all land into a queue as source nodes
## BFS for water cells and use a level variable to remember the level of expansion
## the last expanded one will be the farthest and the final level would be the maximum distance

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        leng = len(grid)
        queue = []
        for row in range(leng):
            for col in range(leng):
                if grid[row][col] == 1:
                    queue.append((row,col))
        
        if len(queue) == 0 or len(queue) == leng*leng:
            return -1
        
        return self.bfs(grid, queue, leng)
    
    def bfs(self, grid, queue, leng):
        visited = set()
        level = -1
        unit = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                visited.add(node)
                for step in unit:
                    nrow = node[0] + step[0]
                    ncol = node[1] + step[1]
                    if nrow >= 0 and nrow < leng and ncol >= 0 and ncol < leng and (nrow,ncol) not in visited and grid[nrow][ncol] == 0:
                        queue.append((nrow, ncol))
                        grid[nrow][ncol] = 1
            level += 1
        return level
                
                
                
        