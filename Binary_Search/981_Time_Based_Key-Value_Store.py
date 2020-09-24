"""
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)
Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)
Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:
Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:
Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 

Note:
All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""

# Approach: Hashmap + Binary Search
# first version: 
# Note: The timestamps for all TimeMap.set operations are strictly increasing. so we actually don't need to sort the list.
"""
    Time Complexity: O(logn ~ n)
    Space Complexity: O(n)

"""
class TimeMap:

    def __init__(self):
        self.map = {}
        self.collect = {}

    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key][timestamp] = value
            self.collect[key].append(timestamp)
            
        else:
            self.map[key] = {timestamp: value}
            self.collect[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        self.collect[key].sort()
        nums = self.collect[key]
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] == timestamp:
                return self.map[key][timestamp]
            elif nums[mid] > timestamp:
                end = mid
            else:
                start = mid
        if timestamp >= nums[start] and timestamp < nums[end]:
            return self.map[key][nums[start]]
        if timestamp >= nums[end]:
            return self.map[key][nums[end]]
        
        return ""

# More concise
class TimeMap:

    def __init__(self):
        self.map = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        nums = self.map[key]
        start = 0
        end = len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid][0] == timestamp:
                return nums[mid][1]
            elif timestamp > nums[mid][0]:
                start = mid
            else:
                end = mid
        if timestamp >= nums[start][0] and timestamp < nums[end][0]:
            return nums[start][1]
        if timestamp >= nums[end][0]:
            return nums[end][1]
        return ""