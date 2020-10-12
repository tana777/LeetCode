"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""

## Approach: DFS + backtracking 
# check if it's duplicated element
"""
Time Complexity:  O(n*n!) 
The total number of steps to complete the exploration is exactly the number of nodes in the tree. 
Therefore, the time complexity of the algorithm is linked directly with the size of the tree.
Space Complexity: O(n*n!)
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        visited = set()
        res = []
        permutation = []
        self.backtrack(nums, n, visited, res, permutation)
        return res
    
    def backtrack(self, nums, n, visited, res, permutation):
        if len(permutation) == n:
            res.append(permutation[:])
            return
        
        for i in range(n):
            if i>0 and nums[i-1] == nums[i] and i-1 in visited:
                continue
            if i not in visited:
                visited.add(i)
                permutation.append(nums[i])
                self.backtrack(nums, n, visited, res, permutation)
                permutation.pop()
                visited.remove(i)
                
                
        