"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
# Approach: DFS + backtracking -- Permutation
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        permutation = []
        n = len(nums)
        used = [False]*n
        self.toFindAllPermutations(results, nums, permutation, used, n)
        return results
    
    def toFindAllPermutations(self, results, nums, permutation, used, n):
        if len(permutation) == n:
            results.append(permutation[:])
            return
        
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            permutation.append(nums[i])
            self.toFindAllPermutations(results, nums, permutation, used, n)
            permutation.pop()
            used[i] = False
        
        
