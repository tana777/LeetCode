"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""

# Method: Two pointers
"""
    Time Complexity: O(n)
    Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        if left + 1 == right:
            return min(height[left], height[right]) * 1
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea