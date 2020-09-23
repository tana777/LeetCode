"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# Approach: DFS + backtracking
"""
Backtracking is an algorithm for finding all solutions by exploring all potential candidates. 
If the solution candidate turns to be not a solution (or at least not the last one), 
backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.
"""
"""
  Time Complexity: O(n*2^n) to generate all subsets and then copy them into output list.
  Space Complexity: O(n*2^n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        combination = []
        n = len(nums)
        self.findAllSubsets(results, nums, combination, n, 0)
        return results
    
    def findAllSubsets(self, results, nums, combination, n, startIdx):
        if  len(combination) == n:
            return
        
        for i in range(startIdx, len(nums)):
            combination.append(nums[i])
            results.append(combination[:])
            self.findAllSubsets(results, nums, combination, n, i+1)
            combination.pop()
        

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        combination = []
        n = len(nums)
        self.findAllSubsets(results, nums, combination, n, 0)
        return results
    
    def findAllSubsets(self, results, nums, combination, n, startIdx):
        if len(combination) <= n:
            results.append(combination[:])

        for i in range(startIdx, len(nums)):
            combination.append(nums[i])
            self.findAllSubsets(results, nums, combination, n, i+1)
            combination.pop()
        
        
        
