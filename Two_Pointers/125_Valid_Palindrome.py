"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
 
Constraints:
s consists only of printable ASCII characters.
"""

# Approach: Two Pointers
"""
    Time Complexity: O(n)
    Space Complexity: o(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
        
# More concise solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = [i.lower() for i in s if i.isalnum()]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True