"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
"""

# This problem is equivalent to 200 Number of Islands.

# Method 1 DFS
""" 
    Iterate over the grid, if we find a number 1 which means it potentially is an island.
    Then we DFS its neighbor, labeled as 0(water) if it's part of the island.
    Finally we find a connected componment (an island) and mark all the nodes to 0.
    we return the number of times labeled to 0 for a connected componment which can 
    be considered as the area of the island.
"""

"""
    Time Complexity: O(n^2) worst case: every one has only one friend, themselves. 
    Space Complexity: O(n^2) recursion call stack
"""

# First version: use global variable to record the area
class Solution:
    def __init__(self):
        self.ct = 0
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        maxArea = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.ct = 0
                    self.dfs(grid, i, j, m, n)
                if self.ct > maxArea:
                    maxArea = self.ct
        return maxArea
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.ct += 1
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j+1, m, n)
        self.dfs(grid, i, j-1, m, n) 
                    
                    
# Improve, let dfs return the area of each island we find
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(grid, i, j, m, n))
        return maxArea

    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.dfs(grid, i+1, j, m, n) + self.dfs(grid, i-1, j, m, n) + \
        self.dfs(grid, i, j-1, m, n) + self.dfs(grid, i, j+1, m, n)

