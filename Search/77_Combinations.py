"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
 
Constraints:
1 <= n <= 20
1 <= k <= n
"""

# Approach: DFS combination
"""
Time Complexity: O(2^n)

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        candidates = [i+1 for i in range(n)]
        print(candidates)
        combination = []
        self.toFindAllCombinations(results, candidates, combination, k, 0)
        return results
    
    def toFindAllCombinations(self, results, candidates, combination, k, startIdx):
        if len(combination) == k:
            results.append(combination[:])
            return
        
        for i in range(startIdx, len(candidates)):
            combination.append(candidates[i])
            self.toFindAllCombinations(results, candidates, combination, k, i+1)
            combination.pop()
        
        