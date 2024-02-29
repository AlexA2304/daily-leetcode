'''
Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], index]
                
            hash[num] = index

# Runtime: 48 ms -- beats 97.17% of users with Python3
# Memory: 17.76 mb -- beats 61.57% of users with Python3