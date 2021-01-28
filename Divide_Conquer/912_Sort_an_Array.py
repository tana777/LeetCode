"""
    Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""


## Method 1 QuickSort - partition
"""
Time complexity: O(nlogn) ~ O(n^2)
Space complexity: O(logn) ~ O(n)
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quickSort(nums, 0, len(nums)-1)
        
    def quickSort(self, nums, low, high):
        if low < high:
            p = self.partition(nums, low, high)
            self.quickSort(nums, low, p-1)
            self.quickSort(nums, p+1, high)
        return
    
    
    def partition(self, nums, low, high):
        pivot = nums[low]
        border = low
        
        for i in range(low, high+1):
            if nums[i] < pivot:
                border += 1
                nums[i], nums[border] = nums[border], nums[i]   
        nums[low], nums[border] = nums[border], nums[low]
        return border 


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return
        l, r = self.partition(nums, start, end)
        self.quickSort(nums, start, r)
        self.quickSort(nums, l, end)
        
    def partition(self, nums, start, end):
        pivot = nums[start] # start, end, random.choice won't affect the correctness of the code
        l, r = start, end
        while r >= l:
            while r >= l and nums[l] < pivot:
                l += 1
            while r >= l and nums[r] > pivot:
                r -= 1
            if r >= l:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1
        return l, r


# Method 2 MergeSort
"""
Time complexity: O(nlogn)
Space complexity: O(logn + n)
"""
# First Version
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            left = self.mergeSort(nums[:mid])
            right = self.mergeSort(nums[mid:])
            return self.merge(left, right)
            
        return nums
    
    def merge(self, l1, l2):
        if not l1 and not l2:
            return l1
        if not l1 or not l2:
            return l1 + l2 
        res = []
        i = j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        if i >= len(l1):
            res.extend(l2[j:])
        if j >= len(l2):
            res.extend(l1[i:])
        return res 
        
# Improvement
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        return self.mergeSort(nums)
        
    def mergeSort(self,nums):
        if len(nums) > 1:
            m = len(nums) // 2
            l = self.mergeSort(nums[:m])
            r = self.mergeSort(nums[m:])
            return self.merge(l, r)
        return nums
        
    def merge(self, list1, list2):
        sorted_list = []
        while list1 and list2:
            if list1[0] <= list2[0]:
                sorted_list.append(list1.pop(0))
            else:
                sorted_list.append(list2.pop(0))
        if list1:
            sorted_list.extend(list1)
        if list2:
            sorted_list.extend(list2)
            
        return sorted_list
            
            
            
# Method 3 Selection sort -- Time Limit Exceeded
"""
    Time Complexity: O(n^2)
    Space Complexity: O(1)

""" 
"""
arr[] = 64 25 12 22 11

// Find the minimum element in arr[0...4]
// and place it at beginning
11 25 12 22 64

// Find the minimum element in arr[1...4]
// and place it at beginning of arr[1...4]
11 12 25 22 64

// Find the minimum element in arr[2...4]
// and place it at beginning of arr[2...4]
11 12 22 25 64

// Find the minimum element in arr[3...4]
// and place it at beginning of arr[3...4]
11 12 22 25 64 
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            minVal = min(nums[i:]) # O(n)
            minIdx = nums[i:].index(minVal) + i
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
        return nums

            
# Method 4 Heapsort
## Heapify procedure can be applied to a node only if its children nodes are heapified. 
# So the heapification must be performed in the bottom-up order.
"""
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # create a max heap
        for i in range(n//2)[::-1]:
            self.heapify(nums, n, i)
            
        # maintain the maxheap and extact the maximum
        for i in range(n)[::-1]:
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        return nums
    
    def heapify(self, nums, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        
        if l < n and nums[l] > nums[largest]:
            largest = l
            
        if r < n and nums[r] > nums[largest]:
            largest = r
            
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            
            self.heapify(nums, n, largest)
    
            
            
# Method 5 Bubble sort 
# Time Limit Exceeded
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            # last i elements already in place
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums


            
# Method 6 Insertion sort 
# Time Limit Exceeded
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        i = j = 0
        while i < n:
            if i == 0:
                i += 1
                j += 1
            while j > 0 and nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
            j = i
        return nums
                