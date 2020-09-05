"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

# Method 1 DFS
""" 
    Iterate over the grid, if we find a number 1 which means it potentially is an island.
    Then we DFS its neighbor, labeled as 0(water) if it's part of the island.
    Finally we find a connected componment (an island) and mark all the nodes to 0.
"""

"""
    Time Complexity: O(mn) iterate over all the value in the grid
    Space Complexity: O(mn) recursion call stack worst cast m*n times
"""

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m==0: return 0
        n = len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island += 1
                    self.dfs(grid, i, j, m, n)

        return island
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i, j-1, m, n)
        self.dfs(grid, i, j+1, m, n)

mySol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
mySol.numIslands(grid)