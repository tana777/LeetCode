"""
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""
# Method 1: Iterate over the list
"""
    Time Complexity: O(n)
    Space Complexity: O(1)
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            if i >= 1 and target > nums[i-1] and target < nums[i]:
                return i
        return len(nums)

# Method 2: Binary Search
"""
    Time Complexity: O(logn)
    Space Complexity: O(1)
"""
class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)-1
        
        while start + 1 < end: # after finish this while loop, there will be two numbers left in the list
            mid = start + (end - start) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        if target > nums[end]:
            return end + 1
        elif target <= nums[start]:
            return start
        else:
            return end