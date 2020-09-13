








# Approach 1 brute force
"""
    For each spot i, if the rain can trap, that means the height of left spot and right spot are both 
    higher than the current ones, and how much water it can trap depends on the height difference between 
    the shorter one of left and right spot and the current spot. So intuitively, for each spot, we are 
    supposed to compute its left highest value and right highest value, choose the small one since it 
    relates to how much water this spot could trap.
    r[i] = min(leftmax, rightmax) - height[i]
    leftmax = max(height[:i])
    rightmax = max(height[i:])
"""

"""
    Time Complexity: O(n^2) For each column, we have to find the maximum left height and right height,
    which takes O(n).
    Space Complexity: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        waterUnits = 0
        if len(height) <= 2:
            return waterUnits
        leftmax = rightmax = curr = 0
        while curr < len(height)-1:
            leftmax = max(leftmax, height[curr])
            rightmax = max(height[curr:]) ## notice we repeatedly scan the array to find the max of right or left
            waterUnits += min(leftmax, rightmax) - height[curr]
            curr = curr + 1
        return waterUnits


# Approach 2: DP prefix max
""" Based on last approach, we find a way to pre-compute the leftmax and rightmax height for
    a given spot. Then iterate over the array to compute the amount of water for each spot.
    Then sum them togeter.
    For simplicity, the first spot, its leftmax value can be considered as itself. 
    and the last spot, its rightmax value can be considered as itself.

    Therefore, querying the max for each spot reduced to O(1) which is a sacrifice of space.
"""
"""
    Time Complexity: O(n)
    Space Compleixty: O(n)
"""

            
class Solution:
    def trap(self, height: List[int]) -> int:
        waterUnits = 0
        n = len(height)
        leftmax = [0 for i in range(n)]
        rightmax = [0 for i in range(n)]
        for i in range(n):
            if i == 0:
                leftmax[i] = height[i]
            else:
                leftmax[i] = max(leftmax[i-1], height[i])
        for i in range(n)[::-1]:
            if i == n-1:
                rightmax[i] = height[i]
            else:
                rightmax[i] = max(rightmax[i+1], height[i])
        for i in range(n):
            waterUnits += min(leftmax[i],rightmax[i]) - height[i]
        return waterUnits

# Approach 3: Two Pointers
""" 
    Use two variables lmax and rmax to track the maximum height of left and right so far.
    Use two pointers l and r to track the leftmost and rightmost position, move l and r
    base on whether lmax < rmax. If lmax < rmax, move l, since how much water the current
    spot could trap depends on lmax. right now rmax may not equal to the right value of its
    maximum. but it doesn't affect the amount of water this spot can trap, as long as it's 
    greater than lmax. The same for rmax, if rmax < lmax, then we should consider to move r.
"""

"""
    Time Complexity: O(n) l and r in total would move n steps
    Space Complexity: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        waterUnits = 0
        if len(height) <= 2:
            return waterUnits
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if lmax < rmax:
                waterUnits += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                waterUnits += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])
        return waterUnits