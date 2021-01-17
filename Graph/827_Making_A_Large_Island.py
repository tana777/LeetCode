"""
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.
"""



# method 1 DFS + islandMap to store known results
class Solution:
    def __init__(self):
        self.maxArea = 0
        self.islandID = 2
        self.islandMap = {}

    def largestIsland(self, grid: List[List[int]]) -> int:
        leng = len(grid)
        for row in range(leng):
            for col in range(leng):
                if grid[row][col] == 1:
                    visited = set()
                    area = self.dfs(grid, row, col, leng, visited)
                    # print(area)
                    self.islandMap[self.islandID] = area
                    self.islandID += 1

        
        for row in range(leng):
            for col in range(leng):
                if grid[row][col] == 0:
                    self.maxArea = max(self.maxArea,self.flipArea(grid, row, col))
        if self.maxArea == 0:
            return leng*leng
        return self.maxArea
                    
                    
        
    def dfs(self, grid, row, col, leng, visited):
        if row < 0 or row >= leng or col < 0 or col >= leng or grid[row][col] == 0 or (row,col) in visited:
            return 0
        visited.add((row,col))
        grid[row][col] = self.islandID
        return 1 + self.dfs(grid, row-1, col, leng, visited) + self.dfs(grid, row+1, col, leng, visited) + self.dfs(grid, row, col-1, leng, visited) + self.dfs(grid, row, col+1, leng, visited)
    

            
    def flipArea(self, grid, row, col):
        area = 1
        islandSet = set()
        unit = [[0,1],[0,-1],[1,0],[-1,0]]
        for step in unit:
            rn = row + step[0]
            cn = col + step[1]
            if rn >= 0 and rn < len(grid) and cn >= 0 and cn < len(grid) and grid[rn][cn] in self.islandMap:
                islandSet.add(grid[rn][cn])
        if islandSet:
            for v in islandSet:
                area += self.islandMap[v]
        return area
            
            
        
         
        

# method 2 UnionFind + 2D to 1D 

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        leng = len(grid)
        maxArea = 0
        uf = UnionFind(leng*leng)
        unit = [[0,1],[0,-1],[1,0],[-1,0]]
        self.computeArea(grid, unit, uf, leng)
        
        for row in range(leng):
            for col in range(leng):
                if grid[row][col] == 0:
                    islandSet = set()
                    area = 1
                    for step in unit:
                        nr = row + step[0]
                        nc = col + step[1]
                        if nr >= 0 and nr < leng and nc >= 0 and nc < leng and grid[nr][nc] == 1:
                            flip = self.twoToOne(nr, nc, leng)
                            islandSet.add((uf.find(flip),uf.sizes[uf.find(flip)]))  
                    for v in islandSet:
                        area += v[1]
                    maxArea = max(maxArea, area)
        
                        
        if maxArea == 0:
            return leng * leng
        return maxArea
        
        
        
    def computeArea(self, grid, unit, uf, leng):
        for row in range(leng):
            for col in range(leng):
                if grid[row][col] == 1:
                    source = self.twoToOne(row, col, leng)
                    for step in unit:
                        nr = row + step[0]
                        nc = col + step[1]
                        if nr >= 0 and nr < leng and nc >= 0 and nc < leng and grid[nr][nc] == 1:
                            target = self.twoToOne(nr, nc, leng)
                            uf.union(source, target)
                            
                        
    def twoToOne(self, row, col, leng):
        return row * leng + col
        


class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
        
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 != root2:
            if self.sizes[root1] >= self.sizes[root2]:
                self.parents[root2] = root1
                self.sizes[root1] += self.sizes[root2]
            else:
                self.parents[root1] = root2
                self.sizes[root2] += self.sizes[root1]
                
    def findRoot(self, v):
        while self.parents[v] != v:
            v = self.parents[v]
        return v
    
    def find(self, v):
        if self.parents[v] == v:
            return v
        root = self.findRoot(v)
        while self.parents[v] != root:
            self.parents[v] = root
            v = self.parents[v]
        return root
            
            
        
