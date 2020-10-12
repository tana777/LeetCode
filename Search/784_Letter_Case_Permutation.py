"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]
 

Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

# Approach: DFS + backtrack
"""
Time Complexity: O(n*2^l) l: number of letters
Space Complexity: O(n) + O(n*2^l) stack + solutions
"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        res = []
        permutation = []
        self.backtrack(list(S), n, 0, res, permutation)
        return res
    
    def backtrack(self, S, n, i, res, permutation):
        if len(permutation) == n:
            res.append(''.join(permutation))
            return
        
        if S[i].isalpha():
            S[i] = S[i].upper()
            permutation.append(S[i])
            self.backtrack(S, n, i+1, res, permutation)
            permutation.pop()
            
            S[i] = S[i].lower()
            permutation.append(S[i])
            self.backtrack(S, n, i+1, res, permutation)
            permutation.pop()
        else:
            permutation.append(S[i])
            self.backtrack(S, n, i+1, res, permutation)
            permutation.pop()
            
            
        
        
