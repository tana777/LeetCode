""" Given an array of size n, find the majority element. 

The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array. """ 


# Method 1 sort
"""
    Time Complexity: O(nlgn)
    Space Complexity: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]



# Method 2 iterate over the list, if prev value is greater than the current, then we find the minimum
# due to the property of rotated and sorted array
"""
    Time Complexity: O(n)
    Space Complexity: O(1)
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]


# Method 3 Divide and Conquer

"""
Idea: Divide and conquer.

Evenly Split the array into two sub-arrays, and find the minimums of them, return the smaller one.
findMin(a[0..n]) = min(findMin(a[0..n/2], a[n/2..n])

Key property:
One of the sub-array will be a sorted array, it takes O(1) to find the minimal element, just the first element.
"""

"""
    Time Complexity: T(n) = O(1) + T(n/2) = O(logn)
    Space Complexity: O(logn)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.minHelper(nums, l = 0, r = len(nums)-1)
    
    def minHelper(self, nums, l, r):
        if l + 1 >= r:
            return min(nums[l], nums[r])
        if nums[l] < nums[r]:
            return nums[l]
        middle = l + (r-l)//2
        return min(self.minHelper(nums, l, middle-1), self.minHelper(nums, middle, r))
        