"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

# Method 1: Combinations via DFS
"""
    Time Complexity: O(4^n), n is the length of the input, 4 is maximum numbers that one digits could represent letters
    Space Complexity: O(4^n + n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        
        digitsLetterMap = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        letterStr = ''
        
        self.letterCombinationHelper(digits, digitsLetterMap, letterStr, res)
        
        return res
    
    def letterCombinationHelper(self, digits, digitsLetterMap, letterStr, res):
        if len(letterStr) == len(digits):
            res.append(letterStr)
            return
        
        idx = int(digits[len(letterStr)])
        for l in digitsLetterMap[idx]:
            letterStr = letterStr + l
            self.letterCombinationHelper(digits, digitsLetterMap, letterStr, res)
            letterStr = letterStr[:len(letterStr)-1]
    
        
        
