"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
## Approach 1: DFS + backtrack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parenthesis = []
        self.toGenerateAllParenthesis(res, parenthesis, n)
        output = self.filterParenthesis(res, n)
        return output
    
    def toGenerateAllParenthesis(self, res, parenthesis, n):
        if len(parenthesis) == 2*n:
            res.append(parenthesis[:])
            return
        
        parenthesis.append('(')
        self.toGenerateAllParenthesis(res, parenthesis, n)
        parenthesis.pop()
        
        parenthesis.append(')')
        self.toGenerateAllParenthesis(res, parenthesis, n)
        parenthesis.pop()
        
    def filterParenthesis(self, res, n):
        output = []
        for p in res:
            if self.checkValid(p):
                output.append(''.join(p))    
        return output
    
    def checkValid(self, parenthesis):  
        pairs = {'(':')'}
        stack = []
        for i in parenthesis:
            if i in pairs:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i != pairs[stack.pop()]:
                    return False
        return stack == []