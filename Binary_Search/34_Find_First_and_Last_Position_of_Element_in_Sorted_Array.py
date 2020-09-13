"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

# Approach: Binary Search
""" Basically, using binary search twice to find the first and last position of target 
    if it exists. Each time, we could get rid of half of elements.
"""
"""
Time complexity : O(log N)
Space complexity : O(1)
All work is done in place, so the overall memory usage is constant.
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if not nums or len(nums) == 0:
            return result
        # find the index of first occurrence of target
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            result[0] = end
        if nums[start] == target:
            result[0] = start
            
        # find the index of last occurrence of target
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif target > nums[mid]:
                start = mid 
            else:
                end = mid
        if nums[start] == target:
            result[1] = start
        if nums[end] == target:
            result[1] = end
            
        return result
        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target == nums[mid]:
                start = mid
            elif target > nums[mid]:
                start = mid
            else:
                end = mid
        print(start,end)
        if target == nums[start] and target == nums[end]:
            while start >= 1:
                if target == nums[start-1]:
                    start -= 1
                else:
                    break
            return [start, end]
        elif target == nums[start]:
            left = start
            while left >= 1:
                if target == nums[left-1]:
                    left -= 1
                else:
                    break
            return [left, start]
        elif target == nums[end]:
            return [end, end]
                
        return [-1,-1]