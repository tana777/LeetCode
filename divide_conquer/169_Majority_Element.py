""" Given an array of size n, find the majority element. 

The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array. """ 

# Method 1 Hash Map 
""" Use a dictionary to record occurrence of each element, at meantime, check if the element 
    appears more than n/2 times. 

    Time complexity : O(n)
    We have to iterate over input list and make a constant time insertion on each iteration.
    Space complexity: O(n)
    For input list nums, its guaranteed to have a majority element, which would at least take
    n/2 + 1 cells, so for maximum, we would have n - (n/2 + 1) distinct keys in the dictionary.
"""

class Solution:
    def majorityElement(self, nums):
        count_dict = dict()
        for ele in nums:
            if ele in count_dict:
                count_dict[ele] = count_dict[ele] + 1
            else:
                count_dict[ele] = 1
            if count_dict[ele] > len(nums) / 2:
                    return ele

mysolution = Solution()
nums = [2,2,1,1,1,2,2]
mysolution.majorityElement(nums)

# Method 2 Sort
""" Sort the input list, then the majority element should in the middle (median) since it's occupied 
    at least n/2 array. If n is even, then two positions n/2 and (n/2)+1 would store it.
"""

""" Time Complexity: O(nlogn)
    Sorting the array would take O(nlogn) time in Python. So it dominates the overall runtime.
    sort and sorted in python are using TimSort which is based on Insertion Sort and Merge Sort.
    It first sorts small pieces using Insertion sort, then merges the pieces using merge sort.
    nums.sort() sorts the list in-place compared with sorted(nums)

    Space Complexity: O(1) or O(n)
    If use in-place nums.sort(), then O(1). Otherwise, we have to make a copy of nums and sort the copy which cost linear additional space.
"""

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

mysolution = Solution()
mysolution.majorityElement(nums)

# Method 3  Divide and Conquer

""" Time complexity: O(nlgn)
    Each recursive call to majorityElementhelper performs two recursive calls on subslices of size n/2
    and two linear scans of length n. Therefore, the time complexity of the divide & conquer approach 
    can be T(n) = 2T(n/2) + 2n. By the master theorem, the recurrence satisfies case 2, so the complexity
    can be analyzed as Θ(nlogn).

    
    Space complexity: O(lgn)
    Recursion stack call would cost memory. The resulting recursion tree is balanced, and therefore
    all paths from the root to a leaf node are of length O(lgn). Because the recursion tree is 
    traversed in a depth-first manner, the space complexity is therefore equivalent to the length of
    the longest path O(lgn).
​	
"""

class Solution:
    def majorityElement(self, nums, l = 0, r = None):
        def majorityElementhelper(l, r):
            # base case 
            if l == r:
                return nums[l]
            
            middle = (r - l) // 2 + l
            left = majorityElementhelper(l, middle)
            right = majorityElementhelper(middle + 1, r)

            if left == right:
                return left
            
            left_count = sum(1 for i in range(l, r + 1) if nums[i] == left)
            right_count = sum(1 for i in range(l, r + 1) if nums[i] == right)
            
            return left if left_count > right_count else right

        return majorityElementhelper(0, len(nums) - 1)

nums = [1,4,6,1,1]
mysolution = Solution()
mysolution.majorityElement(nums)


# Method 4 Boyer-Moore Voting Algorithm

"""
    Finding a Candidate
    The algorithm for the first phase that works in O(n) is known as Moore’s Voting Algorithm. 
    Basic idea of the algorithm is that if each occurrence of an element e can be cancelled with 
    all the other elements that are different from e then e will exist till end
    if it is a majority element.

    Time Complexity: O(n)
    We have to iterate over the array and each iteration, it costs constant time.

    Space Complexity: O(1)
    Boyer-Moore allocates only constant additional memory.
"""

class Solution:
    def majorityElement(self, nums):
        majority = nums[0]
        count = 1
        for ele in nums:
            if majority == ele:
                count = count + 1
            else:
                count = count - 1
            if count == 0:
                majority = ele
                count = 1
        return majority

mysolution = Solution()
nums = [2,4,6,2,2]
mysolution.majorityElement(nums)

# Method 5 Randomization

"""
    Majority element occupies the array over n/2 position, so it should have a high probability
    to catch it when randomly picking up one element from the list.

    Time Complexity: O(n)
    Space Complexity: O(1)
"""
import random

class Solution:
    def majorityElement(self, nums):
        
        while True:
            index = random.randint(0, len(nums)-1)
            count = 0
            for ele in nums:
                if nums[index] == ele:
                    count = count + 1
                if count > len(nums) / 2:
                    return nums[index]


class Solution:
    def majorityElement(self, nums):
        
        while True:
            majority = random.choice(nums)
            count = 0
            for ele in nums:
                if majority == ele:
                    count = count + 1
                if count > len(nums) / 2:
                    return majority

mysolution = Solution()
nums = [2,4,6,2,2]
mysolution.majorityElement(nums)









