"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# Approach: DFS + backtracking
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        combination = []
        n = len(nums)
        nums.sort()
        self.toFindAllSubsets(results, combination, nums, n, 0)
        return results
    
    def toFindAllSubsets(self, results, combination, nums, n, startIdx):
        if len(combination) <= n:
            results.append(combination[:])
            
        for i in range(startIdx, len(nums)):
            if i!= startIdx and nums[i-1] == nums[i]:
                continue
            combination.append(nums[i])
            self.toFindAllSubsets(results, combination, nums, n, i+1)
            combination.pop()
        
