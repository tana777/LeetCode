"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
Each element of candidate is unique.
1 <= target <= 500
"""

# Approach: DFS - combination
## sort array first
## dfs 
## prune tree:
# since we have sorted array, if the current one is greater than target, then the rest of the elements definitely greater than target.
## The same repeated number may be chosen from candidates unlimited number of times.
"""
    Time Complexity: O(2^n) # n: number of elements in candidates list
    Space Complexity: O(k*n) # k: number of elements in the final results list
"""
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        if not candidates or len(candidates) == 0:
            return self.results
        candidates.sort()
        self.combinations = []
        self.toFindCombinationtoTarget(self.results, candidates, self.combinations, target, 0)
        return self.results
    
    def toFindCombinationtoTarget(self, results, candidates, combinations, target, startidx):
        if target == 0:
            results.append(combinations)
            return
        
        for i in range(startidx, len(candidates)):
            if candidates[i] > target:
                break
            combinations.append(candidates[i])
            self.toFindCombinationtoTarget(results, candidates, combinations[:], target-candidates[i], i) # element can be repeatedly used
            combinations.pop()
            
        