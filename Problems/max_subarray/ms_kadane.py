'''
Given an integer array nums, find the subarray
with the largest sum, and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxSoFar = -10000
        maxEndingHere = 0

        for num in nums:
            maxEndingHere += num
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
            if maxEndingHere < 0:
                maxEndingHere = 0
        return maxSoFar
    
# Runtime: 476 ms -- beats 98.54% of users with Python3 ;)
# Memory: 30.86 mb -- beats 82.04% of users with Python3