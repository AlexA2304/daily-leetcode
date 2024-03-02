'''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            pivot = ((right - left) // 2) + left
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot
            else:
                left = pivot + 1
            
        return -1
    
# Runtime: 47 ms -- beats 93.61% of users with Python3
# Memory: 17.76 mb -- beats 64.91% of users with Python3