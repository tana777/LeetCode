"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0
Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
"""
    Time Complexity: Average: O(logn)
                     Worst: O(n)
    Space Complexity
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.minHelp(nums, 0, len(nums)-1)
        
    def minHelp(self, nums, l, r):
        if l + 1 >= r:
            return min(nums[l], nums[r])
        if nums[r] > nums[l]:
            return nums[l]
        mid = l + (r-l)//2
        return min(self.minHelp(nums, l, mid-1), self.minHelp(nums, mid, r))
