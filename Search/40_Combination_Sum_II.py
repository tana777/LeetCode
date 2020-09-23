"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

# Approach: DFS - combination
## sort array first
## dfs 
## prune tree:
# since we have sorted array, if the current one is greater than target, then the rest of the elements definitely greater than target.
## Each number in candidates may only be used once in the combination.
# The solution set must not contain duplicate combinations.


"""
    Time Complexity: O(2^n) # n: number of elements in candidates list
    Space Complexity: O(k*n) # k: number of elements in the final results list
"""
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        if not candidates or len(candidates) == 0:
            return results
        combinations = []
        candidates.sort()
        self.toFindCombinationstoTarget(results, candidates, combinations, target, 0)
        return results
    
    def toFindCombinationstoTarget(self, results, candidates, combinations, target, startidx):
        if target == 0:
            results.append(combinations[:])
            return
        
        for i in range(startidx,len(candidates)):

            if i != startidx and candidates[i]==candidates[i-1]:
                continue # The solution set must not contain duplicate combinations.

            if candidates[i] > target:
                break
            combinations.append(candidates[i])
            self.toFindCombinationstoTarget(results, candidates, combinations, target-candidates[i],i+1) # Each number in candidates may only be used once in the combination.
            combinations.pop()
        