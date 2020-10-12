"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# Approach: Data Structure: stack
"""
we can use stack to help us solve this problem since stack is first in last out. FILO
1. iterate over the input, when it's a left parenthesis, push it to stack
2. when it's a right parenthesis, pop the topmost left parenthesis(if stack is empty, which meams more right parentheses), check if they match
3. after for loop, if stack is not empty, which means more left parentheses in this case
If an input parentheses is not valid, there are three different situation:
A. # left parenthesis > # right parenthese
B. vice versa
C. left != right
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenthesis = {'(':')', '[':']', '{':'}'}
        for i in s:
            if i in parenthesis:
                stack.append(i)
            else:
                if not stack:
                    return False
                if parenthesis[stack.pop()] != i:
                    return False
        return stack == []
        
            
        
                
        
        
