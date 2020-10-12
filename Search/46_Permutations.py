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
"""
Time Complexity: O(n*n!) -- n! permutation results, for each permutation, we use O(n) to get it
Space Complexity: O(n*n!)
If we are not returning an array here so linear space because our recursion will go at maximum n elements deep 
since we make n choices of placement at maximum
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        permutation = []
        visited = set()
        self.backtrack(nums,n,res,permutation,visited)
        return res
    
    def backtrack(self, nums, n, res, permutation, visited):
        if len(permutation) == n:
            res.append(permutation[:])
            return
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                permutation.append(nums[i])
                self.backtrack(nums,n,res,permutation,visited)
                permutation.pop()
                visited.remove(i)

                
        
        
        
        
