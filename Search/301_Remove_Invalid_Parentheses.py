"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

# DFS
# Find number of invalid left and right parentheses 
# so we can use this as condition for backtrack
# check valid parenthesis
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l, r = self.invalidParenthesesNumber(s)
        res = []
        self.backtrack(res, s, l, r, 0)
        return res
        
    def backtrack(self, res, s, l, r, start):
        if l == 0 and r == 0:
            if self.checkValid(list(s)):
                res.append(s)
                return
            
        for i in range(start, len(s)):
            if start != i and s[i] == s[i-1]:
                continue
            if s[i] == '(' or s[i] == ')':
                curr = s
                curr = curr[:i] + curr[i+1:]
                if r > 0 and s[i] == ')':
                    self.backtrack(res, curr, l, r-1, i)
                elif l > 0 and s[i] == '(':
                    self.backtrack(res, curr, l-1, r, i)
                    
        
    def invalidParenthesesNumber(self, s):
        l = r = 0
        for ele in s:
            l += (ele == '(')
            if l == 0:
                r += (ele == ')')
            else:
                l -= (ele == ')')    
        return l, r
            
            
    def getValidParentheses(self, res):
        output = []
        for p in res:
            if self.checkValid(list(p)):
                output.append(''.join(p))
        return output
    
    def checkValid(self, parenthesis):
        stack = []
        pairs = {'(':')'}
        for ele in parenthesis:
            if ele.isalnum():
                continue
            if ele in pairs:
                stack.append(ele)
            else:
                if not stack:
                    return False
                if ele != pairs[stack.pop()]:
                    return False
        return stack == []
 
        
        