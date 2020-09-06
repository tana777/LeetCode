"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. 
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


# Method 1 DFS
""" 
    Iterate over the grid, if we find a number 1 which means it potentially is an island.
    Then we DFS its neighbor, labeled as 0(water) if it's part of the island.
    Finally we find a connected componment (an island) and mark all the nodes to 0.
    we return the number of times labeled to 0 for a connected componment which can 
    be considered as the area of the island.
"""

"""
    Time Complexity: O(mn)
    Space Complexity: O(1) recursion call stack
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        m = len(image)
        n = len(image[0])
        color = image[sr][sc]
        self.dfs(image, sr, sc, m, n, color, newColor)
        return image
    
    def dfs(self, image, i, j, m, n, color, newColor):
        if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != color:
            return
        image[i][j] = newColor
        self.dfs(image, i+1, j, m, n, color, newColor)
        self.dfs(image, i-1, j, m, n, color, newColor)
        self.dfs(image, i, j-1, m, n, color, newColor)
        self.dfs(image, i, j+1, m, n, color, newColor)